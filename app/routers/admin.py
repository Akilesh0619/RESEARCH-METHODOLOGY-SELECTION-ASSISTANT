import os
from typing import Optional
from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from engine.rule_engine import load_rules

router = APIRouter(prefix="/admin")

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("/rules", response_class=HTMLResponse)
def get_admin_rules(
    request: Request,
    effect: Optional[str] = "all",
    search: Optional[str] = None
):
    all_rules = load_rules()

    filtered_rules = []
    for r in all_rules:
        r_effect = r.get("effect", "boost").lower()
        if effect and effect.lower() != "all" and r_effect != effect.lower():
            continue

        if search:
            s = search.lower()
            id_match = s in r.get("id", "").lower()
            method_match = s in r.get("method_id", "").lower()
            reason_match = s in r.get("reason_text", "").lower()
            cond_match = any(
                s in str(k).lower() or s in str(v).lower()
                for k, v in r.get("conditions", {}).items()
            )
            if not (id_match or method_match or reason_match or cond_match):
                continue

        filtered_rules.append(r)

    rule_counts = {
        "all": len(all_rules),
        "boost": sum(1 for r in all_rules if r.get("effect") == "boost"),
        "penalty": sum(1 for r in all_rules if r.get("effect") == "penalty"),
        "hard_exclude": sum(1 for r in all_rules if r.get("effect") == "hard_exclude"),
    }

    user = getattr(request.state, "user", None)
    return templates.TemplateResponse(
        request=request,
        name="admin/rules.html",
        context={
            "active_page": "admin",
            "rules": filtered_rules,
            "current_effect": effect,
            "current_search": search,
            "rule_counts": rule_counts,
            "user": user,
        }
    )

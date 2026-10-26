from typing import Optional, List
from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import os

from app.database import get_db
from app.services import kb_service

router = APIRouter()

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("/kb", response_class=HTMLResponse)
def list_knowledge_base(
    request: Request,
    category: Optional[str] = "all",
    cost: Optional[str] = "all",
    time_req: Optional[str] = "all",
    domain: Optional[str] = "all",
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    methods = kb_service.get_all_methods(
        db,
        category=category,
        cost=cost,
        time_req=time_req,
        domain=domain,
        search=search
    )
    user = getattr(request.state, "user", None)
    return templates.TemplateResponse(
        request=request,
        name="kb/list.html",
        context={
            "active_page": "kb",
            "methods": methods,
            "current_category": category,
            "current_cost": cost,
            "current_time": time_req,
            "current_domain": domain,
            "current_search": search,
            "user": user,
        }
    )


@router.get("/kb/{method_id}", response_class=HTMLResponse)
def get_method_details(
    request: Request,
    method_id: str,
    db: Session = Depends(get_db)
):
    method = kb_service.get_method_by_id(db, method_id)
    if not method:
        raise HTTPException(status_code=404, detail="Research method not found")

    user = getattr(request.state, "user", None)
    return templates.TemplateResponse(
        request=request,
        name="kb/detail.html",
        context={
            "active_page": "kb",
            "method": method,
            "user": user,
        }
    )


@router.get("/compare", response_class=HTMLResponse)
def compare_methods(
    request: Request,
    ids: Optional[str] = None,
    m1: Optional[str] = None,
    m2: Optional[str] = None,
    m3: Optional[str] = None,
    db: Session = Depends(get_db)
):
    all_methods = kb_service.get_all_methods(db)

    method_ids = []
    if ids:
        method_ids = [i.strip() for i in ids.split(",") if i.strip()]
    else:
        if m1:
            method_ids.append(m1)
        if m2:
            method_ids.append(m2)
        if m3:
            method_ids.append(m3)

    # Defaults if none selected
    if not method_ids:
        method_ids = ["survey", "experiment", "case_study"]

    # Limit to 3
    method_ids = method_ids[:3]

    methods = kb_service.get_methods_by_ids(db, method_ids)
    
    # Preserve order of method_ids
    ordered_methods = []
    for mid in method_ids:
        for m in methods:
            if m.id == mid:
                ordered_methods.append(m)
                break

    user = getattr(request.state, "user", None)
    return templates.TemplateResponse(
        request=request,
        name="kb/compare.html",
        context={
            "active_page": "compare",
            "methods": ordered_methods,
            "all_methods": all_methods,
            "user": user,
        }
    )

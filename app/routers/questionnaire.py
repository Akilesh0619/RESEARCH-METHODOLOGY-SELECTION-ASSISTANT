import os
from typing import Optional
from fastapi import APIRouter, Depends, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.services import kb_service, engine_service
from engine.rule_engine import run_recommendation_engine

router = APIRouter()

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("/questionnaire", response_class=HTMLResponse)
def get_questionnaire_view(request: Request):
    user = getattr(request.state, "user", None)
    return templates.TemplateResponse(
        request=request,
        name="questionnaire.html",
        context={
            "active_page": "questionnaire",
            "user": user,
        }
    )


@router.post("/questionnaire")
async def post_questionnaire(
    request: Request,
    db: Session = Depends(get_db)
):
    form_data = await request.form()
    inputs = dict(form_data)

    user = getattr(request.state, "user", None)
    user_id = user.id if user else None

    # Evaluate and persist session in SQLite
    session_id = engine_service.evaluate_and_save_session(
        db,
        inputs=inputs,
        user_id=user_id
    )

    return RedirectResponse(url=f"/results/{session_id}", status_code=303)


@router.get("/results/{session_id}", response_class=HTMLResponse)
def get_results_view(
    request: Request,
    session_id: int,
    db: Session = Depends(get_db)
):
    session = engine_service.get_session_by_id(db, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Recommendation session not found")

    # Fetch method metadata to enrich results
    methods = kb_service.get_all_methods(db)
    methods_dict = {m.id: m for m in methods}

    # Run engine to compute full result hierarchy (top 3, alternatives, disqualified)
    engine_output = run_recommendation_engine(
        session.questionnaire_inputs,
        methods_dict
    )

    user = getattr(request.state, "user", None)
    return templates.TemplateResponse(
        request=request,
        name="results.html",
        context={
            "active_page": "results",
            "session": session,
            "top_methods": engine_output["top_methods"],
            "alternatives": engine_output["alternatives"],
            "disqualified_methods": engine_output["disqualified_methods"],
            "general_warnings": engine_output["general_warnings"],
            "user": user,
        }
    )

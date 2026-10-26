import os
from typing import Optional
from fastapi import APIRouter, Depends, Request, Response, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import RecommendationSession, Review, User, ResearchMethod
from app.services import validation_service, kb_service, engine_service
from engine.rule_engine import run_recommendation_engine

router = APIRouter(prefix="/review")

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("/queue", response_class=HTMLResponse)
def get_review_queue(
    request: Request,
    status: Optional[str] = "all",
    db: Session = Depends(get_db)
):
    query = db.query(RecommendationSession)
    if status and status.lower() != "all":
        query = query.filter(RecommendationSession.review_status == status.lower())

    sessions = query.order_by(RecommendationSession.created_at.desc()).all()
    user = getattr(request.state, "user", None)

    # Count statistics for filter badges
    all_sessions = db.query(RecommendationSession).all()
    status_counts = {
        "all": len(all_sessions),
        "pending": sum(1 for s in all_sessions if s.review_status == "pending"),
        "approved": sum(1 for s in all_sessions if s.review_status == "approved"),
        "rejected": sum(1 for s in all_sessions if s.review_status == "rejected"),
        "needs_revision": sum(1 for s in all_sessions if s.review_status == "needs_revision"),
    }

    return templates.TemplateResponse(
        request=request,
        name="review/queue.html",
        context={
            "active_page": "review",
            "sessions": sessions,
            "current_status": status,
            "status_counts": status_counts,
            "user": user,
        }
    )


@router.get("/session/{session_id}", response_class=HTMLResponse)
def get_session_review_detail(
    request: Request,
    session_id: int,
    db: Session = Depends(get_db)
):
    session = engine_service.get_session_by_id(db, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Recommendation session not found")

    methods = kb_service.get_all_methods(db)
    methods_dict = {m.id: m for m in methods}
    engine_output = run_recommendation_engine(session.questionnaire_inputs, methods_dict)

    user = getattr(request.state, "user", None)
    return templates.TemplateResponse(
        request=request,
        name="review/detail.html",
        context={
            "active_page": "review",
            "session": session,
            "top_methods": engine_output["top_methods"],
            "alternatives": engine_output["alternatives"],
            "all_methods": methods,
            "fired_rules": engine_output["fired_rules"],
            "user": user,
        }
    )


@router.post("/{session_id}")
async def submit_session_review(
    request: Request,
    session_id: int,
    decision: str = Form(...),
    comments: str = Form(...),
    suggested_method_id: Optional[str] = Form(None),
    db: Session = Depends(get_db)
):
    session = engine_service.get_session_by_id(db, session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Recommendation session not found")

    user = getattr(request.state, "user", None)
    if not user:
        # Fallback to demo faculty user
        user = db.query(User).filter(User.role == "faculty").first()
        if not user:
            user = db.query(User).first()

    clean_alt_id = suggested_method_id.strip() if suggested_method_id and suggested_method_id.strip() else None

    # Record review
    review = Review(
        session_id=session.id,
        faculty_id=user.id if user else 1,
        decision=decision.strip().lower(),
        suggested_method_id=clean_alt_id,
        comments=comments.strip()
    )
    db.add(review)

    # Update session status
    session.review_status = decision.strip().lower()
    db.commit()

    return RedirectResponse(url=f"/results/{session.id}", status_code=303)


@router.get("/dashboard", response_class=HTMLResponse)
def get_validation_dashboard(
    request: Request,
    db: Session = Depends(get_db)
):
    benchmark_metrics = validation_service.evaluate_benchmarks(db)
    faculty_metrics = validation_service.get_faculty_validation_metrics(db)
    user = getattr(request.state, "user", None)

    return templates.TemplateResponse(
        request=request,
        name="review/dashboard.html",
        context={
            "active_page": "dashboard",
            "benchmarks": benchmark_metrics,
            "faculty": faculty_metrics,
            "user": user,
        }
    )


@router.get("/export-csv")
def export_csv_data(db: Session = Depends(get_db)):
    csv_content = validation_service.export_validation_csv(db)
    return Response(
        content=csv_content,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=faculty_validation_dataset.csv"}
    )

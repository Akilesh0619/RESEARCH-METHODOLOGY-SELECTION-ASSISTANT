from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from app.models import (
    ResearchMethod,
    RecommendationSession,
    SessionMethod,
    SessionRule
)
from engine.rule_engine import run_recommendation_engine


def evaluate_and_save_session(
    db: Session,
    inputs: Dict[str, Any],
    user_id: Optional[int] = None
) -> int:
    """Runs recommendation engine and records session, suggested methods, and fired rules in database."""
    # Fetch all methods metadata for the engine
    methods = db.query(ResearchMethod).all()
    methods_dict = {m.id: m for m in methods}

    # Run deterministic rule engine
    result = run_recommendation_engine(inputs, methods_dict)

    # Create new recommendation session
    session = RecommendationSession(
        user_id=user_id,
        student_name=inputs.get("student_name", "Anonymous Student"),
        study_title=inputs.get("study_title", "Untitled Research Study"),
        questionnaire_inputs=inputs,
        review_status="pending"
    )
    db.add(session)
    db.flush()  # assign session.id

    # Persist top 3 methods
    for item in result["top_methods"]:
        sm = SessionMethod(
            session_id=session.id,
            method_id=item["method_id"],
            rank=item["rank"],
            match_percentage=item["match_percentage"],
            raw_score=item["raw_score"],
            warnings=item.get("warnings", [])
        )
        db.add(sm)

    # Persist fired rules
    for fr in result["fired_rules"]:
        sr = SessionRule(
            session_id=session.id,
            method_id=fr["method_id"],
            rule_id=fr["rule_id"],
            effect=fr["effect"],
            weight=fr["weight"],
            reason_text=fr["reason_text"]
        )
        db.add(sr)

    db.commit()
    db.refresh(session)
    return session.id


def get_session_by_id(db: Session, session_id: int) -> Optional[RecommendationSession]:
    """Retrieve saved recommendation session by ID with relationships preloaded."""
    return db.query(RecommendationSession).filter(RecommendationSession.id == session_id).first()

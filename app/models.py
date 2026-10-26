from datetime import datetime, timezone
from sqlalchemy import (
    Column, Integer, String, Text, Float, DateTime, ForeignKey, JSON
)
from sqlalchemy.orm import relationship
from app.database import Base


def get_utc_now():
    return datetime.now(timezone.utc)


class ResearchMethod(Base):
    __tablename__ = "research_methods"

    id = Column(String(50), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(String(30), nullable=False, index=True)  # qualitative | quantitative | mixed
    status = Column(String(50), default="draft - needs faculty verification", nullable=False)
    description = Column(Text, nullable=False)
    best_used_when = Column(Text, nullable=False)
    strengths = Column(JSON, default=list)
    limitations = Column(JSON, default=list)
    typical_data_collection = Column(JSON, default=list)
    typical_analysis_techniques = Column(JSON, default=list)
    sample_size_guidance = Column(Text, nullable=False)
    time_required = Column(String(20), nullable=False)  # low | med | high
    cost = Column(String(20), nullable=False)  # low | med | high
    ethical_considerations = Column(Text, nullable=False)
    example_use_cases = Column(JSON, default=list)
    suitable_domains = Column(JSON, default=list)
    references = Column(JSON, default=list)
    updated_at = Column(DateTime, default=get_utc_now, onupdate=get_utc_now)

    session_methods = relationship("SessionMethod", back_populates="method", cascade="all, delete-orphan")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    role = Column(String(20), default="student", nullable=False)  # student | faculty | admin
    full_name = Column(String(100), nullable=False)
    department = Column(String(100), default="Computer Science")
    created_at = Column(DateTime, default=get_utc_now)

    reviews = relationship("Review", back_populates="faculty")
    sessions = relationship("RecommendationSession", back_populates="user")


class RecommendationSession(Base):
    __tablename__ = "recommendation_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    student_name = Column(String(100), default="Anonymous Student")
    study_title = Column(String(200), default="Untitled Research Study")
    questionnaire_inputs = Column(JSON, nullable=False)
    review_status = Column(String(30), default="pending", nullable=False)  # pending | approved | rejected | needs_revision
    created_at = Column(DateTime, default=get_utc_now)

    user = relationship("User", back_populates="sessions")
    suggested_methods = relationship("SessionMethod", back_populates="session", cascade="all, delete-orphan", order_by="SessionMethod.rank")
    fired_rules = relationship("SessionRule", back_populates="session", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="session", cascade="all, delete-orphan")


class SessionMethod(Base):
    __tablename__ = "session_methods"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("recommendation_sessions.id"), nullable=False)
    method_id = Column(String(50), ForeignKey("research_methods.id"), nullable=False)
    rank = Column(Integer, nullable=False)  # 1, 2, 3
    match_percentage = Column(Float, nullable=False)
    raw_score = Column(Float, nullable=False)
    warnings = Column(JSON, default=list)

    session = relationship("RecommendationSession", back_populates="suggested_methods")
    method = relationship("ResearchMethod", back_populates="session_methods")


class SessionRule(Base):
    __tablename__ = "session_rules"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("recommendation_sessions.id"), nullable=False)
    method_id = Column(String(50), nullable=False)
    rule_id = Column(String(50), nullable=False)
    effect = Column(String(30), nullable=False)  # boost | penalty | hard_exclude
    weight = Column(Float, nullable=False)
    reason_text = Column(Text, nullable=False)

    session = relationship("RecommendationSession", back_populates="fired_rules")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("recommendation_sessions.id"), nullable=False)
    faculty_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    decision = Column(String(30), nullable=False)  # approve | reject | needs_revision
    suggested_method_id = Column(String(50), nullable=True)
    comments = Column(Text, nullable=False)
    created_at = Column(DateTime, default=get_utc_now)

    session = relationship("RecommendationSession", back_populates="reviews")
    faculty = relationship("User", back_populates="reviews")


class BenchmarkScenario(Base):
    __tablename__ = "benchmark_scenarios"

    id = Column(Integer, primary_key=True, index=True)
    scenario_id = Column(String(50), unique=True, index=True, nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    domain = Column(String(50), nullable=False)
    questionnaire_inputs = Column(JSON, nullable=False)
    expected_method_ids = Column(JSON, nullable=False)  # list of acceptable/gold standard method IDs
    rationale = Column(Text, nullable=False)
    faculty_contributor = Column(String(100), default="Faculty Committee")
    created_at = Column(DateTime, default=get_utc_now)

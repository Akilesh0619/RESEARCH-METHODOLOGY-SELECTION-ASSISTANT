import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.models import (
    ResearchMethod,
    RecommendationSession,
    SessionMethod,
    SessionRule
)
from app.services import kb_service, engine_service
from engine.rule_engine import load_rules, run_recommendation_engine


# In-memory test DB
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    kb_service.seed_methods_from_yaml(db)
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def methods_dict(db_session):
    methods = db_session.query(ResearchMethod).all()
    return {m.id: m for m in methods}


def test_rules_catalog_count():
    """Verify rules.yaml contains at least 40 meaningful declarative rules."""
    rules = load_rules(force_reload=True)
    assert len(rules) >= 40, f"Expected at least 40 rules, found {len(rules)}"
    
    # Verify required rule attributes
    for r in rules:
        assert "id" in r
        assert "conditions" in r
        assert "method_id" in r
        assert "effect" in r
        assert r["effect"] in ["boost", "penalty", "hard_exclude"]
        assert "weight" in r
        assert "reason_text" in r
        assert len(r["reason_text"]) > 10, f"Rule {r['id']} has insubstantial reason text"


def test_hypothesis_quantitative_recommendation(methods_dict):
    """Testing causal hypotheses with numerical data & full control should recommend Experiment in Top 3."""
    inputs = {
        "study_title": "Effect of UI Feedback on Reaction Times",
        "student_name": "Student A",
        "research_objective": "explain_test_hypothesis",
        "data_type": "numerical",
        "control_over_variables": "full",
        "sample_size_available": "30_to_100",
        "time_available": "3_to_6_months",
        "budget": "medium",
        "participant_access": "easy",
        "existing_theory": "well_established",
        "study_timeframe": "one_time",
        "domain": "engineering",
        "ethical_sensitivity": "low"
    }

    result = run_recommendation_engine(inputs, methods_dict)
    top_ids = [m["method_id"] for m in result["top_methods"]]
    assert "experiment" in top_ids, f"Expected 'experiment' in Top 3, got {top_ids}"
    assert result["top_methods"][0]["match_percentage"] > 60.0
    assert len(result["top_methods"][0]["why_this_method"]) >= 1


def test_exploratory_qualitative_recommendation(methods_dict):
    """Exploratory study with textual data and no prior theory should favor Grounded Theory or Phenomenology."""
    inputs = {
        "study_title": "Exploring Coping Strategies of First-Gen Students",
        "student_name": "Student B",
        "research_objective": "explore",
        "data_type": "textual_narrative",
        "control_over_variables": "none",
        "sample_size_available": "10_to_30",
        "time_available": "3_to_6_months",
        "budget": "low",
        "participant_access": "easy",
        "existing_theory": "none",
        "study_timeframe": "one_time",
        "domain": "education",
        "ethical_sensitivity": "medium"
    }

    result = run_recommendation_engine(inputs, methods_dict)
    top_ids = [m["method_id"] for m in result["top_methods"]]
    assert any(m in top_ids for m in ["grounded_theory", "phenomenology", "case_study", "semi_structured_interview"])


def test_artifact_engineering_recommendation(methods_dict):
    """Building and evaluating an engineering artifact should rank Design Science Research as #1."""
    inputs = {
        "study_title": "A Distributed Consensus Protocol for IoT Clusters",
        "student_name": "Engineer Alex",
        "research_objective": "build_evaluate_artifact",
        "data_type": "numerical",
        "control_over_variables": "full",
        "sample_size_available": "30_to_100",
        "time_available": "3_to_6_months",
        "budget": "medium",
        "participant_access": "easy",
        "existing_theory": "limited",
        "study_timeframe": "one_time",
        "domain": "engineering",
        "ethical_sensitivity": "low"
    }

    result = run_recommendation_engine(inputs, methods_dict)
    assert result["top_methods"][0]["method_id"] == "design_science_research"


def test_secondary_literature_review_recommendation(methods_dict):
    """Reviewing literature with secondary data only should recommend Systematic Literature Review / Meta-analysis."""
    inputs = {
        "study_title": "Systematic Review of Explainable AI in Medicine",
        "student_name": "Researcher Dana",
        "research_objective": "review_literature",
        "data_type": "textual_narrative",
        "control_over_variables": "none",
        "sample_size_available": "30_to_100",
        "time_available": "3_to_6_months",
        "budget": "low",
        "participant_access": "none_secondary_only",
        "existing_theory": "limited",
        "study_timeframe": "one_time",
        "domain": "health",
        "ethical_sensitivity": "low"
    }

    result = run_recommendation_engine(inputs, methods_dict)
    top_ids = [m["method_id"] for m in result["top_methods"]]
    assert "systematic_literature_review" in top_ids


def test_hard_exclude_sample_size_under_10(methods_dict):
    """Sample size under 10 must hard exclude Survey and Meta-analysis."""
    inputs = {
        "study_title": "Micro Clinical Case",
        "student_name": "User C",
        "research_objective": "describe",
        "data_type": "numerical",
        "control_over_variables": "none",
        "sample_size_available": "under_10",
        "time_available": "1_to_3_months",
        "budget": "low",
        "participant_access": "easy",
        "existing_theory": "limited",
        "study_timeframe": "one_time",
        "domain": "health",
        "ethical_sensitivity": "medium"
    }

    result = run_recommendation_engine(inputs, methods_dict)
    top_ids = [m["method_id"] for m in result["top_methods"]]
    assert "survey" not in top_ids
    assert "meta_analysis" not in top_ids

    disq_ids = [m["method_id"] for m in result["disqualified_methods"] if m["disqualified"]]
    assert "survey" in disq_ids
    assert "meta_analysis" in disq_ids


def test_hard_exclude_time_under_1_month(methods_dict):
    """Time available under 1 month must hard exclude Longitudinal Study and Ethnography."""
    inputs = {
        "study_title": "Rapid Sprint Review",
        "student_name": "User D",
        "research_objective": "describe",
        "data_type": "numerical",
        "control_over_variables": "none",
        "sample_size_available": "30_to_100",
        "time_available": "under_1_month",
        "budget": "low",
        "participant_access": "easy",
        "existing_theory": "well_established",
        "study_timeframe": "over_time",
        "domain": "management",
        "ethical_sensitivity": "low"
    }

    result = run_recommendation_engine(inputs, methods_dict)
    top_ids = [m["method_id"] for m in result["top_methods"]]
    assert "longitudinal_study" not in top_ids
    assert "ethnography" not in top_ids

    disq_ids = [m["method_id"] for m in result["disqualified_methods"] if m["disqualified"]]
    assert "longitudinal_study" in disq_ids
    assert "ethnography" in disq_ids


def test_hard_exclude_no_participant_access(methods_dict):
    """No participant access (secondary only) must hard exclude Field Interviews, Focus Groups, and Experiments."""
    inputs = {
        "study_title": "Archival Analysis",
        "student_name": "User E",
        "research_objective": "describe",
        "data_type": "textual_narrative",
        "control_over_variables": "none",
        "sample_size_available": "30_to_100",
        "time_available": "1_to_3_months",
        "budget": "low",
        "participant_access": "none_secondary_only",
        "existing_theory": "limited",
        "study_timeframe": "one_time",
        "domain": "social_science",
        "ethical_sensitivity": "low"
    }

    result = run_recommendation_engine(inputs, methods_dict)
    disq_ids = [m["method_id"] for m in result["disqualified_methods"] if m["disqualified"]]
    assert "semi_structured_interview" in disq_ids
    assert "focus_group" in disq_ids
    assert "experiment" in disq_ids


def test_conflicting_rules_resolution(methods_dict):
    """
    Conflicting scenario: user wants to explore (normally qual), but collects numerical data,
    has over 100 sample size, and well-established theory.
    Engine must resolve weights smoothly without crashing or negative scores.
    """
    inputs = {
        "study_title": "Conflicting Requirements Case",
        "student_name": "Tester",
        "research_objective": "explore",
        "data_type": "numerical",
        "control_over_variables": "none",
        "sample_size_available": "over_100",
        "time_available": "1_to_3_months",
        "budget": "medium",
        "participant_access": "easy",
        "existing_theory": "well_established",
        "study_timeframe": "one_time",
        "domain": "management",
        "ethical_sensitivity": "low"
    }

    result = run_recommendation_engine(inputs, methods_dict)
    assert len(result["top_methods"]) == 3
    for m in result["top_methods"]:
        assert 0.0 <= m["match_percentage"] <= 100.0
        assert m["rank"] in [1, 2, 3]


def test_session_db_persistence(db_session):
    """Test full persistence of recommendation session, suggested methods, and fired rules in database."""
    inputs = {
        "study_title": "Examining Micro-Learning in Software Training",
        "student_name": "Rohan Patel",
        "research_objective": "evaluate_intervention",
        "data_type": "both",
        "control_over_variables": "partial",
        "sample_size_available": "30_to_100",
        "time_available": "3_to_6_months",
        "budget": "low",
        "participant_access": "easy",
        "existing_theory": "limited",
        "study_timeframe": "over_time",
        "domain": "education",
        "ethical_sensitivity": "low"
    }

    session_id = engine_service.evaluate_and_save_session(db_session, inputs)
    assert session_id is not None

    saved_session = db_session.query(RecommendationSession).filter_by(id=session_id).first()
    assert saved_session is not None
    assert saved_session.study_title == inputs["study_title"]
    assert saved_session.review_status == "pending"

    # Verify suggested methods persisted
    methods = db_session.query(SessionMethod).filter_by(session_id=session_id).all()
    assert len(methods) >= 3

    # Verify fired rules persisted
    rules = db_session.query(SessionRule).filter_by(session_id=session_id).all()
    assert len(rules) > 0
    assert any(r.reason_text for r in rules)

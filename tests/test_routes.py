import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.models import ResearchMethod, User, RecommendationSession
from app.services import kb_service, auth_service, validation_service
from app.main import app

from sqlalchemy.pool import StaticPool

# Test DB setup
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    kb_service.seed_methods_from_yaml(db)
    auth_service.seed_demo_users(db)
    validation_service.seed_benchmark_scenarios(db)
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client(test_db):
    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()



def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Research Methodology Selection Assistant" in response.text


def test_auth_login_page(client):
    response = client.get("/auth/login")
    assert response.status_code == 200
    assert "Sign In" in response.text
    assert "student123" in response.text


def test_auth_login_successful(client):
    response = client.post(
        "/auth/login",
        data={"username": "faculty", "password": "faculty123"},
        follow_redirects=False
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/review/queue"
    assert "session_token" in response.cookies


def test_auth_login_invalid(client):
    response = client.post(
        "/auth/login",
        data={"username": "wrong", "password": "wrongpassword"},
        follow_redirects=False
    )
    assert response.status_code == 401
    assert "Invalid username or password" in response.text


def test_auth_logout(client):
    response = client.get("/auth/logout", follow_redirects=False)
    assert response.status_code == 303
    assert response.headers["location"] == "/"


def test_review_queue_page(client):
    response = client.get("/review/queue")
    assert response.status_code == 200
    assert "Faculty Review Queue" in response.text


def test_validation_dashboard_page(client):
    response = client.get("/review/dashboard")
    assert response.status_code == 200
    assert "Empirical Validation Dashboard" in response.text
    assert "30 Benchmark Academic Research Scenarios" in response.text


def test_export_validation_csv(client):
    response = client.get("/review/export-csv")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]
    assert "Session ID,Created At,Student Name" in response.text


def test_admin_rules_page(client):
    response = client.get("/admin/rules")
    assert response.status_code == 200
    assert "Declarative Rules Catalog" in response.text
    assert "Target Method" in response.text


def test_questionnaire_submission_and_faculty_review_flow(client, test_db):
    # 1. Submit questionnaire
    q_data = {
        "study_title": "Automated Bug Localization with Language Models",
        "student_name": "Test Student",
        "research_objective": "build_evaluate_artifact",
        "data_type": "numerical",
        "control_over_variables": "full",
        "sample_size_available": "30_to_100",
        "time_available": "3_to_6_months",
        "budget": "low",
        "participant_access": "easy",
        "existing_theory": "limited",
        "study_timeframe": "one_time",
        "domain": "engineering",
        "ethical_sensitivity": "low"
    }
    resp = client.post("/questionnaire", data=q_data, follow_redirects=False)
    assert resp.status_code == 303
    session_url = resp.headers["location"]
    session_id = int(session_url.split("/")[-1])

    # 2. Results page loads
    res_page = client.get(f"/results/{session_id}")
    assert res_page.status_code == 200
    assert "Automated Bug Localization" in res_page.text
    assert "Top 3 Recommended Research Methodologies" in res_page.text

    # 3. Faculty review detail page loads
    rev_detail = client.get(f"/review/session/{session_id}")
    assert rev_detail.status_code == 200
    assert "Faculty Evaluation: Session" in rev_detail.text

    # 4. Faculty submits review
    rev_post = client.post(
        f"/review/{session_id}",
        data={
            "decision": "approve",
            "comments": "Methodology is well-suited for automated software engineering artifact evaluation.",
            "suggested_method_id": ""
        },
        follow_redirects=False
    )
    assert rev_post.status_code == 303

    # 5. Check session updated to approved
    test_db.expire_all()
    updated_session = test_db.query(RecommendationSession).filter(RecommendationSession.id == session_id).first()
    assert updated_session.review_status == "approve"


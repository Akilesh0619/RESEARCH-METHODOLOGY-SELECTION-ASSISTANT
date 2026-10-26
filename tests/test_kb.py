import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.models import ResearchMethod
from app.services import kb_service
from app.main import app

# Test database
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    kb_service.seed_methods_from_yaml(db)
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="module")
def client(test_db):
    def override_get_db():
        try:
            yield test_db
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()


def test_seed_methods_count(test_db):
    """Verify that exactly 20 methods specified in requirements are seeded."""
    methods = test_db.query(ResearchMethod).all()
    assert len(methods) == 20, f"Expected 20 methods, got {len(methods)}"


def test_seed_methods_status_and_content(test_db):
    """Verify all methods are marked as draft and have textbook references."""
    methods = test_db.query(ResearchMethod).all()
    expected_categories = {"qualitative", "quantitative", "mixed"}
    
    for m in methods:
        assert m.status == "draft - needs faculty verification", f"Method {m.id} has incorrect status {m.status}"
        assert m.category in expected_categories, f"Method {m.id} has unknown category {m.category}"
        assert len(m.strengths) >= 2, f"Method {m.id} has fewer than 2 strengths"
        assert len(m.limitations) >= 2, f"Method {m.id} has fewer than 2 limitations"
        assert len(m.example_use_cases) >= 2, f"Method {m.id} must have at least 2 example use cases"
        assert len(m.references) >= 1, f"Method {m.id} has no textbook references"
        assert m.sample_size_guidance, f"Method {m.id} missing sample size guidance"


def test_kb_list_page(client):
    """Verify KB list page returns HTTP 200 and displays methods."""
    response = client.get("/kb")
    assert response.status_code == 200
    assert "Research Methodology Knowledge Base" in response.text
    assert "Survey Research" in response.text
    assert "True Experimental Design" in response.text


def test_kb_category_filter(client):
    """Verify category filtering works correctly."""
    response = client.get("/kb?category=qualitative")
    assert response.status_code == 200
    assert "Case Study Research" in response.text
    assert "Grounded Theory" in response.text
    # Quantitative should not show in qualitative filtered result
    assert "True Experimental Design" not in response.text


def test_kb_search_filter(client):
    """Verify keyword search returns matching method."""
    response = client.get("/kb?search=PRISMA")
    assert response.status_code == 200
    assert "Systematic Literature Review" in response.text


def test_kb_detail_page(client):
    """Verify individual method detail page loads correctly."""
    response = client.get("/kb/experiment")
    assert response.status_code == 200
    assert "True Experimental Design" in response.text
    assert "Key Strengths" in response.text
    assert "Methodological Limitations" in response.text
    assert "draft - needs faculty verification" in response.text


def test_kb_detail_not_found(client):
    """Verify 404 is returned for non-existent method."""
    response = client.get("/kb/unknown_method_xyz")
    assert response.status_code == 404


def test_compare_page(client):
    """Verify side-by-side compare page renders multiple methods."""
    response = client.get("/compare?ids=survey,experiment,case_study")
    assert response.status_code == 200
    assert "Side-by-Side Methodology Comparison" in response.text
    assert "Survey Research" in response.text
    assert "True Experimental Design" in response.text
    assert "Case Study Research" in response.text

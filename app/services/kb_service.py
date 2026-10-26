import os
import yaml
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models import ResearchMethod

METHODS_YAML_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "data",
    "methods.yaml"
)


def seed_methods_from_yaml(db: Session) -> int:
    """Seeds research methodologies from data/methods.yaml into SQLite database if not already present."""
    if not os.path.exists(METHODS_YAML_PATH):
        raise FileNotFoundError(f"Methods YAML file not found at {METHODS_YAML_PATH}")

    with open(METHODS_YAML_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    methods_list = data.get("methods", [])
    count = 0

    for m in methods_list:
        existing = db.query(ResearchMethod).filter(ResearchMethod.id == m["id"]).first()
        if not existing:
            new_method = ResearchMethod(
                id=m["id"],
                name=m["name"],
                category=m.get("category", "mixed"),
                status=m.get("status", "draft - needs faculty verification"),
                description=m["description"],
                best_used_when=m.get("best_used_when", ""),
                strengths=m.get("strengths", []),
                limitations=m.get("limitations", []),
                typical_data_collection=m.get("typical_data_collection", []),
                typical_analysis_techniques=m.get("typical_analysis_techniques", []),
                sample_size_guidance=m.get("sample_size_guidance", ""),
                time_required=m.get("time_required", "med"),
                cost=m.get("cost", "low"),
                ethical_considerations=m.get("ethical_considerations", ""),
                example_use_cases=m.get("example_use_cases", []),
                suitable_domains=m.get("suitable_domains", []),
                references=m.get("references", []),
            )
            db.add(new_method)
            count += 1
        else:
            # Update fields to reflect any data updates
            existing.name = m["name"]
            existing.category = m.get("category", existing.category)
            existing.status = m.get("status", existing.status)
            existing.description = m["description"]
            existing.best_used_when = m.get("best_used_when", "")
            existing.strengths = m.get("strengths", [])
            existing.limitations = m.get("limitations", [])
            existing.typical_data_collection = m.get("typical_data_collection", [])
            existing.typical_analysis_techniques = m.get("typical_analysis_techniques", [])
            existing.sample_size_guidance = m.get("sample_size_guidance", "")
            existing.time_required = m.get("time_required", "med")
            existing.cost = m.get("cost", "low")
            existing.ethical_considerations = m.get("ethical_considerations", "")
            existing.example_use_cases = m.get("example_use_cases", [])
            existing.suitable_domains = m.get("suitable_domains", [])
            existing.references = m.get("references", [])

    db.commit()
    return count


def get_all_methods(
    db: Session,
    category: Optional[str] = None,
    cost: Optional[str] = None,
    time_req: Optional[str] = None,
    domain: Optional[str] = None,
    search: Optional[str] = None
) -> List[ResearchMethod]:
    """Retrieve filtered and searched research methodologies."""
    query = db.query(ResearchMethod)

    if category and category.lower() != "all":
        query = query.filter(ResearchMethod.category == category.lower())

    if cost and cost.lower() != "all":
        query = query.filter(ResearchMethod.cost == cost.lower())

    if time_req and time_req.lower() != "all":
        query = query.filter(ResearchMethod.time_required == time_req.lower())

    methods = query.order_by(ResearchMethod.name.asc()).all()

    # In-memory post filtering for JSON-based fields and text search
    filtered = []
    for m in methods:
        # Domain check (JSON list)
        if domain and domain.lower() != "all":
            domains_lower = [d.lower() for d in (m.suitable_domains or [])]
            if domain.lower() not in domains_lower:
                continue

        # Search term check
        if search:
            s = search.lower()
            name_match = s in m.name.lower()
            desc_match = s in m.description.lower()
            best_match = s in (m.best_used_when or "").lower()
            tags_match = any(s in str(tech).lower() for tech in (m.typical_analysis_techniques or []))
            if not (name_match or desc_match or best_match or tags_match):
                continue

        filtered.append(m)

    return filtered


def get_method_by_id(db: Session, method_id: str) -> Optional[ResearchMethod]:
    """Get a single method by ID."""
    return db.query(ResearchMethod).filter(ResearchMethod.id == method_id).first()


def get_methods_by_ids(db: Session, method_ids: List[str]) -> List[ResearchMethod]:
    """Get multiple methods by their IDs for compare view."""
    return db.query(ResearchMethod).filter(ResearchMethod.id.in_(method_ids)).all()

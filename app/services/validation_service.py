import os
import io
import csv
import yaml
from typing import Dict, List, Any, Tuple
from sqlalchemy.orm import Session
from app.models import (
    BenchmarkScenario,
    RecommendationSession,
    ResearchMethod,
    Review
)
from engine.rule_engine import run_recommendation_engine

BENCHMARKS_YAML_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "data",
    "benchmark_scenarios.yaml"
)


def seed_benchmark_scenarios(db: Session) -> int:
    """Seeds the 30 benchmark academic research scenarios into SQLite."""
    if not os.path.exists(BENCHMARKS_YAML_PATH):
        return 0

    with open(BENCHMARKS_YAML_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    benchmarks = data.get("benchmarks", [])
    count = 0

    for b in benchmarks:
        existing = db.query(BenchmarkScenario).filter(BenchmarkScenario.scenario_id == b["scenario_id"]).first()
        if not existing:
            new_b = BenchmarkScenario(
                scenario_id=b["scenario_id"],
                title=b["title"],
                domain=b.get("domain", "other"),
                description=b["description"],
                questionnaire_inputs=b["questionnaire_inputs"],
                expected_method_ids=b["expected_method_ids"],
                rationale=b.get("rationale", ""),
                faculty_contributor=b.get("faculty_contributor", "Faculty Committee")
            )
            db.add(new_b)
            count += 1
        else:
            existing.title = b["title"]
            existing.domain = b.get("domain", existing.domain)
            existing.description = b["description"]
            existing.questionnaire_inputs = b["questionnaire_inputs"]
            existing.expected_method_ids = b["expected_method_ids"]
            existing.rationale = b.get("rationale", existing.rationale)
            existing.faculty_contributor = b.get("faculty_contributor", existing.faculty_contributor)

    db.commit()
    return count


def evaluate_benchmarks(db: Session) -> Dict[str, Any]:
    """Runs the rule engine against all 30 benchmark scenarios and computes Top-1 and Top-3 accuracy."""
    benchmarks = db.query(BenchmarkScenario).order_by(BenchmarkScenario.id.asc()).all()
    methods = db.query(ResearchMethod).all()
    methods_dict = {m.id: m for m in methods}

    total = len(benchmarks)
    if total == 0:
        return {
            "total": 0,
            "top1_matches": 0,
            "top3_matches": 0,
            "top1_accuracy": 0.0,
            "top3_accuracy": 0.0,
            "scenario_results": []
        }

    top1_count = 0
    top3_count = 0
    scenario_results = []

    for b in benchmarks:
        result = run_recommendation_engine(b.questionnaire_inputs, methods_dict)
        top_methods = result["top_methods"]
        top_ids = [m["method_id"] for m in top_methods]
        rank1_id = top_ids[0] if top_ids else None

        expected_ids = b.expected_method_ids or []
        is_top1 = rank1_id in expected_ids
        is_top3 = any(tid in expected_ids for tid in top_ids)

        if is_top1:
            top1_count += 1
        if is_top3:
            top3_count += 1

        scenario_results.append({
            "scenario_id": b.scenario_id,
            "title": b.title,
            "domain": b.domain,
            "expected_method_ids": expected_ids,
            "top1_recommended": rank1_id,
            "top3_recommended": top_ids,
            "is_top1_match": is_top1,
            "is_top3_match": is_top3,
            "rationale": b.rationale,
            "contributor": b.faculty_contributor
        })

    top1_accuracy = round((top1_count / total) * 100, 1)
    top3_accuracy = round((top3_count / total) * 100, 1)

    return {
        "total": total,
        "top1_matches": top1_count,
        "top3_matches": top3_count,
        "top1_accuracy": top1_accuracy,
        "top3_accuracy": top3_accuracy,
        "scenario_results": scenario_results
    }


def get_faculty_validation_metrics(db: Session) -> Dict[str, Any]:
    """Computes real-time review statistics, approval rates, and override analysis from database."""
    sessions = db.query(RecommendationSession).all()
    reviews = db.query(Review).all()

    total_sessions = len(sessions)
    pending_count = sum(1 for s in sessions if s.review_status == "pending")
    approved_count = sum(1 for s in sessions if s.review_status == "approved")
    rejected_count = sum(1 for s in sessions if s.review_status == "rejected")
    revision_count = sum(1 for s in sessions if s.review_status == "needs_revision")

    reviewed_total = approved_count + rejected_count + revision_count
    approval_rate = round((approved_count / reviewed_total) * 100, 1) if reviewed_total > 0 else 0.0

    # Overridden methods analysis (when faculty suggests an alternative method)
    override_counts: Dict[str, int] = {}
    for r in reviews:
        if r.suggested_method_id:
            override_counts[r.suggested_method_id] = override_counts.get(r.suggested_method_id, 0) + 1

    # Method category distribution in recommendations
    category_counts = {"quantitative": 0, "qualitative": 0, "mixed": 0}
    for s in sessions:
        if s.suggested_methods:
            primary_method = s.suggested_methods[0].method
            if primary_method and primary_method.category in category_counts:
                category_counts[primary_method.category] += 1

    return {
        "total_sessions": total_sessions,
        "reviewed_total": reviewed_total,
        "pending_count": pending_count,
        "approved_count": approved_count,
        "rejected_count": rejected_count,
        "revision_count": revision_count,
        "approval_rate": approval_rate,
        "override_counts": override_counts,
        "category_counts": category_counts
    }


def export_validation_csv(db: Session) -> str:
    """Generates standard CSV content of all recommendation sessions and faculty review outcomes."""
    output = io.StringIO()
    writer = csv.writer(output)

    # Header row
    writer.writerow([
        "Session ID",
        "Created At",
        "Student Name",
        "Study Title",
        "Academic Domain",
        "Research Objective",
        "Data Type",
        "Sample Size Available",
        "Time Available",
        "Rank 1 Method",
        "Rank 1 Match %",
        "Rank 2 Method",
        "Rank 2 Match %",
        "Rank 3 Method",
        "Rank 3 Match %",
        "Faculty Review Status",
        "Faculty Reviewer",
        "Faculty Decision",
        "Faculty Suggested Alternative",
        "Faculty Comments"
    ])

    sessions = db.query(RecommendationSession).order_by(RecommendationSession.id.asc()).all()

    for s in sessions:
        inputs = s.questionnaire_inputs or {}
        top_methods = s.suggested_methods or []

        m1 = top_methods[0].method_id if len(top_methods) > 0 else "N/A"
        p1 = f"{top_methods[0].match_percentage}%" if len(top_methods) > 0 else "0%"
        m2 = top_methods[1].method_id if len(top_methods) > 1 else "N/A"
        p2 = f"{top_methods[1].match_percentage}%" if len(top_methods) > 1 else "0%"
        m3 = top_methods[2].method_id if len(top_methods) > 2 else "N/A"
        p3 = f"{top_methods[2].match_percentage}%" if len(top_methods) > 2 else "0%"

        latest_review = s.reviews[-1] if s.reviews else None
        reviewer_name = latest_review.faculty.full_name if (latest_review and latest_review.faculty) else "Unassigned"
        decision = latest_review.decision if latest_review else "Pending"
        suggested_alt = latest_review.suggested_method_id if latest_review else ""
        comments = latest_review.comments if latest_review else ""

        writer.writerow([
            s.id,
            s.created_at.strftime("%Y-%m-%d %H:%M:%S") if s.created_at else "",
            s.student_name,
            s.study_title,
            inputs.get("domain", ""),
            inputs.get("research_objective", ""),
            inputs.get("data_type", ""),
            inputs.get("sample_size_available", ""),
            inputs.get("time_available", ""),
            m1, p1,
            m2, p2,
            m3, p3,
            s.review_status,
            reviewer_name,
            decision,
            suggested_alt,
            comments
        ])

    return output.getvalue()

import os
import yaml
from typing import Dict, List, Any, Optional
from engine.scoring import calculate_method_scores, generate_feasibility_warnings

RULES_YAML_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data",
    "rules.yaml"
)

# In-memory cached rules
_CACHED_RULES: Optional[List[Dict[str, Any]]] = None


def load_rules(force_reload: bool = False) -> List[Dict[str, Any]]:
    """Loads declarative rules from data/rules.yaml."""
    global _CACHED_RULES
    if _CACHED_RULES is not None and not force_reload:
        return _CACHED_RULES

    if not os.path.exists(RULES_YAML_PATH):
        raise FileNotFoundError(f"Rules YAML file not found at {RULES_YAML_PATH}")

    with open(RULES_YAML_PATH, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    rules = data.get("rules", [])
    _CACHED_RULES = rules
    return rules


def evaluate_condition(expected: Any, actual: Any) -> bool:
    """Evaluates if actual user input satisfies expected rule condition."""
    if actual is None:
        return False

    if isinstance(expected, list):
        return str(actual).lower() in [str(x).lower() for x in expected]

    return str(expected).strip().lower() == str(actual).strip().lower()


def run_recommendation_engine(
    inputs: Dict[str, Any],
    methods_dict: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Main evaluation pipeline:
    1. Loads declarative rules.
    2. Matches conditions against inputs.
    3. Calculates raw and normalized match scores.
    4. Ranks top 3 methods, alternatives (ranks 4-5), and disqualified methods.
    5. Returns transparent explanations and feasibility warnings.
    """
    rules = load_rules()
    all_method_ids = list(methods_dict.keys())

    fired_rules: List[Dict[str, Any]] = []

    for r in rules:
        conditions = r.get("conditions", {})
        matches = True
        for attr, expected in conditions.items():
            actual = inputs.get(attr)
            if not evaluate_condition(expected, actual):
                matches = False
                break

        if matches:
            fired_rules.append({
                "rule_id": r["id"],
                "method_id": r["method_id"],
                "effect": r.get("effect", "boost"),
                "weight": float(r.get("weight", 15.0)),
                "reason_text": r.get("reason_text", "")
            })

    raw_scores, match_percentages, disqualified, method_warnings = calculate_method_scores(
        rules, fired_rules, all_method_ids
    )

    # Sort eligible methods
    eligible_methods = []
    disqualified_methods = []

    for mid in all_method_ids:
        method_meta = methods_dict.get(mid, {})
        method_name = getattr(method_meta, "name", mid)
        category = getattr(method_meta, "category", "mixed")
        description = getattr(method_meta, "description", "")

        # Collect fired reasons for this specific method
        why_reasons = [
            fr["reason_text"]
            for fr in fired_rules
            if fr["method_id"] == mid and fr["effect"] == "boost"
        ]

        item = {
            "method_id": mid,
            "method_name": method_name,
            "category": category,
            "match_percentage": match_percentages[mid],
            "raw_score": raw_scores[mid],
            "description": description,
            "why_this_method": why_reasons,
            "warnings": method_warnings[mid],
            "disqualified": disqualified[mid],
        }

        if disqualified[mid] or match_percentages[mid] == 0:
            disqualified_methods.append(item)
        else:
            eligible_methods.append(item)

    # Sort eligible by match_percentage descending, then raw_score descending
    eligible_methods.sort(
        key=lambda x: (x["match_percentage"], x["raw_score"]),
        reverse=True
    )

    # Assign ranks
    for idx, em in enumerate(eligible_methods, start=1):
        em["rank"] = idx

    top_3 = eligible_methods[:3]
    alternatives = eligible_methods[3:5]

    general_warnings = generate_feasibility_warnings(inputs)

    return {
        "study_title": inputs.get("study_title", "Untitled Research Study"),
        "student_name": inputs.get("student_name", "Anonymous Student"),
        "top_methods": top_3,
        "alternatives": alternatives,
        "disqualified_methods": disqualified_methods,
        "fired_rules": fired_rules,
        "general_warnings": general_warnings,
    }

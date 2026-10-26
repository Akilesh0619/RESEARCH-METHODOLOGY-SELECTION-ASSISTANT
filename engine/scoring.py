from typing import Dict, List, Any, Tuple


def calculate_method_scores(
    rules: List[Dict[str, Any]],
    fired_rules: List[Dict[str, Any]],
    all_method_ids: List[str]
) -> Tuple[Dict[str, float], Dict[str, float], Dict[str, bool], Dict[str, List[str]]]:
    """
    Computes raw scores, normalized 0-100% match percentages, disqualification flags,
    and specific warnings for all research methodologies.
    """
    # 1. Calculate maximum potential boost per method from the rules catalog
    max_potential_boost: Dict[str, float] = {mid: 0.0 for mid in all_method_ids}
    for r in rules:
        mid = r.get("method_id")
        if mid in max_potential_boost and r.get("effect") == "boost":
            max_potential_boost[mid] += float(r.get("weight", 0.0))

    # Ensure baseline denominator floor so small weights don't artificially score 100%
    for mid in max_potential_boost:
        # Benchmark max is either 75% of total possible boosts or minimum 70 points
        max_potential_boost[mid] = max(70.0, max_potential_boost[mid] * 0.75)

    # 2. Accumulate fired rules per method
    raw_scores: Dict[str, float] = {mid: 0.0 for mid in all_method_ids}
    disqualified: Dict[str, bool] = {mid: False for mid in all_method_ids}
    method_warnings: Dict[str, List[str]] = {mid: [] for mid in all_method_ids}

    for fr in fired_rules:
        mid = fr["method_id"]
        effect = fr["effect"]
        weight = float(fr["weight"])

        if effect == "hard_exclude":
            disqualified[mid] = True
            method_warnings[mid].append(f"Disqualified: {fr['reason_text']}")
        elif effect == "boost":
            raw_scores[mid] += weight
        elif effect == "penalty":
            raw_scores[mid] -= weight
            method_warnings[mid].append(f"Caveat (-{int(weight)}% match): {fr['reason_text']}")

    # 3. Compute normalized 0-100% match score
    match_percentages: Dict[str, float] = {}
    for mid in all_method_ids:
        if disqualified[mid]:
            match_percentages[mid] = 0.0
            raw_scores[mid] = 0.0
        else:
            raw = raw_scores[mid]
            if raw <= 0:
                match_percentages[mid] = 0.0
            else:
                denom = max_potential_boost.get(mid, 80.0)
                norm = (raw / denom) * 100.0
                # Clamp to 10% - 98% to reflect realistic probabilistic confidence
                clamped = min(98.0, max(15.0, norm))
                match_percentages[mid] = round(clamped, 1)

    return raw_scores, match_percentages, disqualified, method_warnings


def generate_feasibility_warnings(inputs: Dict[str, Any]) -> List[str]:
    """Generates general advisory warnings based on questionnaire constraint combinations."""
    warnings = []

    # Short time + high ambition
    if inputs.get("time_available") == "under_1_month":
        warnings.append(
            "Short Timeframe Advisory: Completing empirical human participant data collection in under 1 month is high-risk. Focus on secondary data, existing archives, or pre-tested rapid survey instruments."
        )

    # Low budget + primary data
    if inputs.get("budget") == "low" and inputs.get("sample_size_available") == "over_100":
        warnings.append(
            "Budget Alert: Recruiting and incentivizing over 100 participants with low budget requires digital convenience sampling (e.g. social networks, student cohorts) rather than paid panels."
        )

    # High ethical sensitivity
    if inputs.get("ethical_sensitivity") == "high":
        warnings.append(
            "Ethics Clearance: Studies with high ethical sensitivity will require Institutional Review Board (IRB) / Ethics Committee clearance, signed participant consent forms, and data anonymization."
        )

    # No participant access + primary objective
    if inputs.get("participant_access") == "none_secondary_only" and inputs.get("research_objective") in ["explore", "evaluate_intervention"]:
        warnings.append(
            "Access Constraint: You indicated no direct access to participants. Ensure your exploratory or intervention questions can be answered via documented case archives or published literature."
        )

    return warnings

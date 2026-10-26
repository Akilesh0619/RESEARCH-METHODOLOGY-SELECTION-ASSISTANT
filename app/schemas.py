from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class ReferenceItem(BaseModel):
    author: str
    year: Any
    title: str
    publisher_or_journal: str


class UseCaseItem(BaseModel):
    domain: str
    title: str
    scenario: str


class ResearchMethodBase(BaseModel):
    id: str
    name: str
    category: str
    status: str
    description: str
    best_used_when: str
    strengths: List[str]
    limitations: List[str]
    typical_data_collection: List[str]
    typical_analysis_techniques: List[str]
    sample_size_guidance: str
    time_required: str
    cost: str
    ethical_considerations: str
    example_use_cases: List[UseCaseItem]
    suitable_domains: List[str]
    references: List[ReferenceItem]


class ResearchMethodOut(ResearchMethodBase):
    pass


class QuestionnaireInput(BaseModel):
    student_name: Optional[str] = "Anonymous Student"
    study_title: Optional[str] = "Untitled Research Study"
    research_objective: str  # explore | describe | explain_test_hypothesis | predict | evaluate_intervention | build_evaluate_artifact | review_literature
    data_type: str  # numerical | textual_narrative | both
    control_over_variables: str  # full | partial | none
    sample_size_available: str  # under_10 | 10_to_30 | 30_to_100 | over_100
    time_available: str  # under_1_month | 1_to_3_months | 3_to_6_months | over_6_months
    budget: str  # low | medium | high
    participant_access: str  # easy | difficult | none_secondary_only
    existing_theory: str  # well_established | limited | none
    study_timeframe: str  # one_time | over_time
    domain: str  # engineering | management | education | health | social_science | other
    ethical_sensitivity: str  # low | medium | high


class FiredRuleOut(BaseModel):
    rule_id: str
    method_id: str
    effect: str
    weight: float
    reason_text: str


class RankedMethodOut(BaseModel):
    method_id: str
    method_name: str
    category: str
    rank: int
    match_percentage: float
    raw_score: float
    description: str
    why_this_method: List[str]
    warnings: List[str]
    disqualified: bool = False


class RecommendationResult(BaseModel):
    session_id: Optional[int] = None
    study_title: str
    student_name: str
    top_methods: List[RankedMethodOut]
    alternatives: List[RankedMethodOut]
    disqualified_methods: List[RankedMethodOut]
    fired_rules: List[FiredRuleOut]
    general_warnings: List[str]


class ReviewCreate(BaseModel):
    session_id: int
    decision: str  # approve | reject | needs_revision
    suggested_method_id: Optional[str] = None
    comments: str


class BenchmarkScenarioOut(BaseModel):
    id: int
    scenario_id: str
    title: str
    description: str
    domain: str
    questionnaire_inputs: Dict[str, Any]
    expected_method_ids: List[str]
    rationale: str
    faculty_contributor: str

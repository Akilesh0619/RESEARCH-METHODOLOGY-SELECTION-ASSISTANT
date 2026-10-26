// Client-side Rule Engine & Scoring Pipeline for GitHub Pages
// Identical deterministic logic matching engine/rule_engine.py and engine/scoring.py

function evaluateCondition(expected, actual) {
  if (actual === undefined || actual === null) return false;
  if (Array.isArray(expected)) {
    const actLower = String(actual).toLowerCase();
    return expected.some(x => String(x).toLowerCase() === actLower);
  }
  return String(expected).trim().toLowerCase() === String(actual).trim().toLowerCase();
}

function calculateMethodScores(rules, firedRules, allMethodIds) {
  const maxPotentialBoost = {};
  allMethodIds.forEach(mid => { maxPotentialBoost[mid] = 0.0; });

  rules.forEach(r => {
    const mid = r.method_id;
    if (mid in maxPotentialBoost && r.effect === 'boost') {
      maxPotentialBoost[mid] += parseFloat(r.weight || 0.0);
    }
  });

  allMethodIds.forEach(mid => {
    maxPotentialBoost[mid] = Math.max(70.0, maxPotentialBoost[mid] * 0.75);
  });

  const rawScores = {};
  const disqualified = {};
  const methodWarnings = {};
  allMethodIds.forEach(mid => {
    rawScores[mid] = 0.0;
    disqualified[mid] = false;
    methodWarnings[mid] = [];
  });

  firedRules.forEach(fr => {
    const mid = fr.method_id;
    const effect = fr.effect;
    const weight = parseFloat(fr.weight);

    if (effect === 'hard_exclude') {
      disqualified[mid] = true;
      methodWarnings[mid].push(`Disqualified: ${fr.reason_text}`);
    } else if (effect === 'boost') {
      rawScores[mid] += weight;
    } else if (effect === 'penalty') {
      rawScores[mid] -= weight;
      methodWarnings[mid].push(`Caveat (-${Math.round(weight)}% match): ${fr.reason_text}`);
    }
  });

  const matchPercentages = {};
  allMethodIds.forEach(mid => {
    if (disqualified[mid]) {
      matchPercentages[mid] = 0.0;
      rawScores[mid] = 0.0;
    } else {
      const raw = rawScores[mid];
      if (raw <= 0) {
        matchPercentages[mid] = 0.0;
      } else {
        const denom = maxPotentialBoost[mid] || 80.0;
        const norm = (raw / denom) * 100.0;
        const clamped = Math.min(98.0, Math.max(15.0, norm));
        matchPercentages[mid] = Math.round(clamped * 10) / 10;
      }
    }
  });

  return { rawScores, matchPercentages, disqualified, methodWarnings };
}

function generateFeasibilityWarnings(inputs) {
  const warnings = [];
  if (inputs.time_available === 'under_1_month') {
    warnings.push("Short Timeframe Advisory: Completing empirical human participant data collection in under 1 month is high-risk. Focus on secondary data, existing archives, or pre-tested rapid survey instruments.");
  }
  if (inputs.budget === 'low' && inputs.sample_size_available === 'over_100') {
    warnings.push("Budget Alert: Recruiting and incentivizing over 100 participants with low budget requires digital convenience sampling (e.g. social networks, student cohorts) rather than paid panels.");
  }
  if (inputs.ethical_sensitivity === 'high') {
    warnings.push("Ethics Clearance: Studies with high ethical sensitivity will require Institutional Review Board (IRB) / Ethics Committee clearance, signed participant consent forms, and data anonymization.");
  }
  if (inputs.participant_access === 'none_secondary_only' && (inputs.research_objective === 'explore' || inputs.research_objective === 'evaluate_intervention')) {
    warnings.push("Access Constraint: You indicated no direct access to participants. Ensure your exploratory or intervention questions can be answered via documented case archives or published literature.");
  }
  return warnings;
}

function runRecommendationEngine(inputs) {
  const rules = RULES_DATA;
  const methods = METHODS_DATA;
  const methodsDict = {};
  methods.forEach(m => { methodsDict[m.id] = m; });
  const allMethodIds = Object.keys(methodsDict);

  const firedRules = [];

  rules.forEach(r => {
    const conditions = r.conditions || {};
    let matches = true;
    for (const [attr, expected] of Object.entries(conditions)) {
      const actual = inputs[attr];
      if (!evaluateCondition(expected, actual)) {
        matches = false;
        break;
      }
    }
    if (matches) {
      firedRules.push({
        rule_id: r.id,
        method_id: r.method_id,
        effect: r.effect || 'boost',
        weight: parseFloat(r.weight || 15.0),
        reason_text: r.reason_text || ''
      });
    }
  });

  const { rawScores, matchPercentages, disqualified, methodWarnings } = calculateMethodScores(rules, firedRules, allMethodIds);

  const eligibleMethods = [];
  const disqualifiedMethods = [];

  allMethodIds.forEach(mid => {
    const meta = methodsDict[mid] || {};
    const whyReasons = firedRules
      .filter(fr => fr.method_id === mid && fr.effect === 'boost')
      .map(fr => fr.reason_text);

    const item = {
      method_id: mid,
      method_name: meta.name || mid,
      category: meta.category || 'mixed',
      match_percentage: matchPercentages[mid],
      raw_score: rawScores[mid],
      description: meta.description || '',
      why_this_method: whyReasons,
      warnings: methodWarnings[mid],
      disqualified: disqualified[mid]
    };

    if (disqualified[mid] || matchPercentages[mid] === 0) {
      disqualifiedMethods.push(item);
    } else {
      eligibleMethods.push(item);
    }
  });

  eligibleMethods.sort((a, b) => {
    if (b.match_percentage !== a.match_percentage) {
      return b.match_percentage - a.match_percentage;
    }
    return b.raw_score - a.raw_score;
  });

  eligibleMethods.forEach((em, idx) => {
    em.rank = idx + 1;
  });

  return {
    study_title: inputs.study_title || 'Untitled Research Study',
    student_name: inputs.student_name || 'Anonymous Student',
    top_methods: eligibleMethods.slice(0, 3),
    alternatives: eligibleMethods.slice(3, 5),
    disqualified_methods: disqualifiedMethods,
    fired_rules: firedRules,
    general_warnings: generateFeasibilityWarnings(inputs)
  };
}

function evaluateBenchmarks() {
  const benchmarks = BENCHMARKS_DATA;
  let top1Count = 0;
  let top3Count = 0;
  const scenarioResults = [];

  benchmarks.forEach(b => {
    const res = runRecommendationEngine(b.questionnaire_inputs);
    const topIds = res.top_methods.map(m => m.method_id);
    const rank1Id = topIds.length > 0 ? topIds[0] : null;
    const expected = b.expected_method_ids || [];

    const isTop1 = expected.includes(rank1Id);
    const isTop3 = topIds.some(id => expected.includes(id));

    if (isTop1) top1Count++;
    if (isTop3) top3Count++;

    scenarioResults.push({
      scenario_id: b.scenario_id,
      title: b.title,
      domain: b.domain,
      expected_method_ids: expected,
      top1_recommended: rank1Id,
      top3_recommended: topIds,
      is_top1_match: isTop1,
      is_top3_match: isTop3,
      rationale: b.rationale,
      contributor: b.faculty_contributor
    });
  });

  const total = benchmarks.length;
  return {
    total,
    top1_matches: top1Count,
    top3_matches: top3Count,
    top1_accuracy: Math.round((top1Count / total) * 1000) / 10,
    top3_accuracy: Math.round((top3Count / total) * 1000) / 10,
    scenario_results: scenarioResults
  };
}

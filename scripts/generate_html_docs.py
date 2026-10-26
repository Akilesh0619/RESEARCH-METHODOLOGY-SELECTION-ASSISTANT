import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS_DIR = os.path.join(BASE_DIR, "docs")

NAV_HTML = """
  <!-- Navigation Header -->
  <nav class="navbar navbar-expand-lg navbar-light bg-white border-bottom sticky-top py-2">
    <div class="container">
      <a class="navbar-brand navbar-brand-custom" href="index.html">
        <i class="bi bi-diagram-3-fill fs-4 text-primary"></i>
        <span>MethodAssist</span>
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navMain">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navMain">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 ms-lg-3">
          <li class="nav-item">
            <a class="nav-link {nav_home}" href="index.html">
              <i class="bi bi-house me-1"></i> Home
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link {nav_kb}" href="kb.html">
              <i class="bi bi-book me-1"></i> Knowledge Base
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link {nav_compare}" href="compare.html">
              <i class="bi bi-arrow-left-right me-1"></i> Compare
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link text-primary fw-semibold {nav_questionnaire}" href="questionnaire.html">
              <i class="bi bi-magic me-1"></i> Get Recommendations
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link {nav_dashboard}" href="dashboard.html">
              <i class="bi bi-graph-up me-1"></i> Validation Dashboard
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link {nav_rules}" href="rules.html">
              <i class="bi bi-sliders me-1"></i> Rules Catalog
            </a>
          </li>
        </ul>

        <div class="d-flex align-items-center gap-2">
          <a href="https://github.com/Akilesh0619/RESEARCH-METHODOLOGY-SELECTION-ASSISTANT" target="_blank" class="btn btn-outline-dark btn-sm d-flex align-items-center gap-1">
            <i class="bi bi-github"></i>
            <span>GitHub Repository</span>
          </a>
        </div>
      </div>
    </div>
  </nav>
"""

FOOTER_HTML = """
  <!-- Global Footer -->
  <footer class="bg-white border-top py-4 mt-auto">
    <div class="container text-center text-muted small">
      <div class="row align-items-center">
        <div class="col-md-6 text-md-start mb-2 mb-md-0">
          <strong>Research Methodology Selection Assistant</strong> • College Mini Project
          <br>
          <span class="text-secondary">Transparent Rule-Based Engine (No ML / No LLMs) • Citations from Creswell, Kothari, Yin, Saunders</span>
        </div>
        <div class="col-md-6 text-md-end">
          <span class="badge bg-light text-dark border me-2"><i class="bi bi-shield-check text-success"></i> Deterministic Engine</span>
          <span class="badge bg-light text-dark border"><i class="bi bi-patch-check text-primary"></i> GitHub Pages Live</span>
        </div>
      </div>
    </div>
  </footer>
"""

def make_page(title, content, active="home", extra_scripts=""):
    nav = NAV_HTML.format(
        nav_home="active" if active == "home" else "",
        nav_kb="active" if active == "kb" else "",
        nav_compare="active" if active == "compare" else "",
        nav_questionnaire="active" if active == "questionnaire" else "",
        nav_dashboard="active" if active == "dashboard" else "",
        nav_rules="active" if active == "rules" else ""
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - MethodAssist</title>
  <meta name="description" content="Transparent, rule-based recommendation assistant for academic research methodologies with faculty validation.">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <link rel="stylesheet" href="static/css/style.css">
</head>
<body>
  {nav}

  <main class="py-4">
    <div class="container">
      {content}
    </div>
  </main>

  {FOOTER_HTML}

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script src="static/js/data.js"></script>
  <script src="static/js/engine.js"></script>
  {extra_scripts}
</body>
</html>
"""

# 1. INDEX.HTML
index_content = """
<div class="hero-gradient mb-5">
  <div class="row align-items-center">
    <div class="col-lg-8">
      <span class="badge bg-white text-primary fw-bold text-uppercase px-3 py-2 rounded-pill mb-3">
        <i class="bi bi-mortarboard-fill me-1"></i> Academic Decision Support System
      </span>
      <h1 class="display-5 fw-bold mb-3">Research Methodology Selection Assistant</h1>
      <p class="lead mb-4 text-white-50">
        Empowering students and researchers to choose the most suitable research methodology for their thesis or project. Powered by a transparent, deterministic <strong>rule-based engine</strong> with explainable reasoning and literature citations.
      </p>
      <div class="d-flex flex-wrap gap-3">
        <a href="questionnaire.html" class="btn btn-light btn-lg text-primary fw-bold shadow-sm px-4">
          <i class="bi bi-play-circle-fill me-2"></i> Start Questionnaire
        </a>
        <a href="kb.html" class="btn btn-outline-light btn-lg px-4">
          <i class="bi bi-journal-bookmark me-2"></i> Explore 20 Methodologies
        </a>
      </div>
    </div>
    <div class="col-lg-4 text-center mt-4 mt-lg-0">
      <div class="p-4 bg-white bg-opacity-10 rounded-4 border border-white border-opacity-25 shadow-sm text-start">
        <h6 class="text-uppercase text-white-50 fw-bold small mb-3">System Specifications</h6>
        <div class="d-flex align-items-center gap-3 mb-3">
          <i class="bi bi-database-check fs-2 text-warning"></i>
          <div>
            <div class="fw-bold fs-5">20 Curated Methods</div>
            <div class="small text-white-50">Quantitative, Qualitative & Mixed</div>
          </div>
        </div>
        <div class="d-flex align-items-center gap-3 mb-3">
          <i class="bi bi-diagram-3 fs-2 text-info"></i>
          <div>
            <div class="fw-bold fs-5">66 Declarative Rules</div>
            <div class="small text-white-50">100% Explainable & Transparent</div>
          </div>
        </div>
        <div class="d-flex align-items-center gap-3">
          <i class="bi bi-patch-check-fill fs-2 text-success"></i>
          <div>
            <div class="fw-bold fs-5">30 Benchmark Scenarios</div>
            <div class="small text-white-50">100% Top-3 Evaluation Accuracy</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<div class="mb-5">
  <div class="text-center mb-4">
    <h3 class="fw-bold">How MethodAssist Works</h3>
    <p class="text-muted">A three-stage transparent pipeline designed for academic integrity</p>
  </div>
  <div class="row g-4">
    <div class="col-md-4">
      <div class="custom-card p-4 h-100">
        <div class="rounded-circle bg-primary bg-opacity-10 text-primary d-inline-flex p-3 mb-3 fs-4">
          <i class="bi bi-ui-checks"></i>
        </div>
        <h5 class="fw-bold">1. Study Questionnaire</h5>
        <p class="text-muted small">
          Answer an 11-dimension survey about your study's objectives, data type, participant access, sample size, time, and budget.
        </p>
      </div>
    </div>
    <div class="col-md-4">
      <div class="custom-card p-4 h-100">
        <div class="rounded-circle bg-success bg-opacity-10 text-success d-inline-flex p-3 mb-3 fs-4">
          <i class="bi bi-cpu"></i>
        </div>
        <h5 class="fw-bold">2. Rule Engine Scoring</h5>
        <p class="text-muted small">
          An external declarative ruleset computes weighted boosts, penalties, and hard constraints to calculate normalized match percentages with detailed "Why" explanations.
        </p>
      </div>
    </div>
    <div class="col-md-4">
      <div class="custom-card p-4 h-100">
        <div class="rounded-circle bg-info bg-opacity-10 text-info d-inline-flex p-3 mb-3 fs-4">
          <i class="bi bi-check2-circle"></i>
        </div>
        <h5 class="fw-bold">3. Empirical Benchmarks</h5>
        <p class="text-muted small">
          Calibrated against 30 published textbook scenarios from Creswell, Kothari, and Yin, achieving high empirical fidelity.
        </p>
      </div>
    </div>
  </div>
</div>
"""
with open(os.path.join(DOCS_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(make_page("Home", index_content, active="home"))

# 2. KB.HTML
kb_content = """
<div class="d-flex flex-wrap justify-content-between align-items-center mb-4">
  <div>
    <h2 class="fw-bold mb-1"><i class="bi bi-book text-primary me-2"></i>Research Methodology Knowledge Base</h2>
    <p class="text-muted mb-0">Explore 20 peer-reviewed research methodologies spanning quantitative, qualitative, and mixed paradigms.</p>
  </div>
  <a href="compare.html" class="btn btn-outline-primary mt-3 mt-md-0">
    <i class="bi bi-arrow-left-right me-1"></i> Side-by-Side Compare
  </a>
</div>

<!-- Filter Bar -->
<div class="filter-bar mb-4">
  <div class="row g-3 align-items-center">
    <div class="col-md-7">
      <div class="d-flex flex-wrap gap-2 align-items-center" id="categoryFilters">
        <span class="text-muted small fw-semibold me-2">Category:</span>
        <button class="btn btn-sm btn-primary rounded-pill filter-btn" data-cat="all">All (20)</button>
        <button class="btn btn-sm btn-outline-primary rounded-pill filter-btn" data-cat="quantitative">Quantitative (8)</button>
        <button class="btn btn-sm btn-outline-success rounded-pill filter-btn" data-cat="qualitative">Qualitative (7)</button>
        <button class="btn btn-sm btn-outline-info text-dark rounded-pill filter-btn" data-cat="mixed">Mixed Methods (5)</button>
      </div>
    </div>
    <div class="col-md-5">
      <div class="input-group">
        <span class="input-group-text bg-white"><i class="bi bi-search text-muted"></i></span>
        <input type="text" id="kbSearch" class="form-control" placeholder="Search by name, technique, or keyword...">
      </div>
    </div>
  </div>
</div>

<!-- Methods Cards Grid -->
<div class="row g-4" id="methodsGrid"></div>
"""

kb_script = """
<script>
  let activeCat = 'all';
  let searchTerm = '';

  function renderMethods() {
    const grid = document.getElementById('methodsGrid');
    const filtered = METHODS_DATA.filter(m => {
      if (activeCat !== 'all' && m.category !== activeCat) return false;
      if (searchTerm) {
        const s = searchTerm.toLowerCase();
        const nMatch = (m.name || '').toLowerCase().includes(s);
        const dMatch = (m.description || '').toLowerCase().includes(s);
        const bMatch = (m.best_used_when || '').toLowerCase().includes(s);
        const tMatch = (m.typical_analysis_techniques || []).some(t => String(t).toLowerCase().includes(s));
        if (!nMatch && !dMatch && !bMatch && !tMatch) return false;
      }
      return true;
    });

    if (filtered.length === 0) {
      grid.innerHTML = `<div class="col-12 text-center py-5 text-muted"><i class="bi bi-search fs-1 mb-2 d-block"></i>No methodologies matched your filter criteria.</div>`;
      return;
    }

    grid.innerHTML = filtered.map(m => `
      <div class="col-md-6 col-lg-4">
        <div class="custom-card p-4 h-100 d-flex flex-column method-card border-top border-3 ${m.category === 'quantitative' ? 'border-primary' : m.category === 'qualitative' ? 'border-success' : 'border-info'}">
          <div class="d-flex justify-content-between align-items-center mb-2">
            <span class="badge badge-${m.category} text-capitalize">${m.category}</span>
            <span class="small text-muted"><i class="bi bi-clock me-1"></i>${m.time_required === 'low' ? 'Quick' : m.time_required === 'med' ? 'Medium' : 'Extended'}</span>
          </div>
          <h5 class="fw-bold mb-2">${m.name}</h5>
          <p class="text-muted small card-text mb-3">${m.description}</p>
          
          <div class="mb-3">
            <span class="small fw-semibold text-dark d-block mb-1">Key Strengths:</span>
            <ul class="small text-muted mb-0 ps-3">
              ${(m.strengths || []).slice(0, 2).map(s => `<li>${s}</li>`).join('')}
            </ul>
          </div>

          <div class="mt-auto pt-2 border-top d-flex justify-content-between align-items-center">
            <span class="small text-muted">Cost: <strong class="text-capitalize text-dark">${m.cost}</strong></span>
            <a href="compare.html?m1=${m.id}" class="btn btn-sm btn-outline-primary">Compare</a>
          </div>
        </div>
      </div>
    `).join('');
  }

  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      document.querySelectorAll('.filter-btn').forEach(b => {
        b.className = 'btn btn-sm rounded-pill filter-btn ' + (b === e.target ? 'btn-primary' : 'btn-outline-secondary');
      });
      activeCat = e.target.getAttribute('data-cat');
      renderMethods();
    });
  });

  document.getElementById('kbSearch').addEventListener('input', (e) => {
    searchTerm = e.target.value.trim();
    renderMethods();
  });

  renderMethods();
</script>
"""
with open(os.path.join(DOCS_DIR, "kb.html"), "w", encoding="utf-8") as f:
    f.write(make_page("Knowledge Base", kb_content, active="kb", extra_scripts=kb_script))

# 3. COMPARE.HTML
compare_content = """
<div class="d-flex flex-wrap justify-content-between align-items-center mb-4">
  <div>
    <h2 class="fw-bold mb-1"><i class="bi bi-arrow-left-right text-primary me-2"></i>Side-by-Side Methodology Comparison</h2>
    <p class="text-muted mb-0">Directly contrast assumptions, sample sizes, analysis methods, and ethics across 3 methodologies.</p>
  </div>
  <a href="kb.html" class="btn btn-outline-secondary btn-sm mt-3 mt-md-0">
    <i class="bi bi-book me-1"></i> Browse Catalog
  </a>
</div>

<div class="custom-card p-4 mb-4">
  <div class="row g-3 align-items-center">
    <div class="col-md-4">
      <label class="form-label small fw-semibold">Method 1</label>
      <select id="selectM1" class="form-select"></select>
    </div>
    <div class="col-md-4">
      <label class="form-label small fw-semibold">Method 2</label>
      <select id="selectM2" class="form-select"></select>
    </div>
    <div class="col-md-4">
      <label class="form-label small fw-semibold">Method 3</label>
      <select id="selectM3" class="form-select"></select>
    </div>
  </div>
</div>

<div class="custom-card overflow-hidden">
  <div class="table-responsive">
    <table class="table table-bordered compare-table align-middle mb-0" id="compareTable">
      <thead id="compareHead"></thead>
      <tbody id="compareBody"></tbody>
    </table>
  </div>
</div>
"""

compare_script = """
<script>
  function populateSelects() {
    const s1 = document.getElementById('selectM1');
    const s2 = document.getElementById('selectM2');
    const s3 = document.getElementById('selectM3');

    const opts = METHODS_DATA.map(m => `<option value="${m.id}">${m.name} (${m.category})</option>`).join('');
    s1.innerHTML = opts;
    s2.innerHTML = opts;
    s3.innerHTML = opts;

    s1.value = 'survey';
    s2.value = 'experiment';
    s3.value = 'case_study';

    s1.addEventListener('change', renderCompare);
    s2.addEventListener('change', renderCompare);
    s3.addEventListener('change', renderCompare);
  }

  function renderCompare() {
    const id1 = document.getElementById('selectM1').value;
    const id2 = document.getElementById('selectM2').value;
    const id3 = document.getElementById('selectM3').value;

    const m1 = METHODS_DATA.find(m => m.id === id1) || METHODS_DATA[0];
    const m2 = METHODS_DATA.find(m => m.id === id2) || METHODS_DATA[1];
    const m3 = METHODS_DATA.find(m => m.id === id3) || METHODS_DATA[2];

    const methods = [m1, m2, m3];

    document.getElementById('compareHead').innerHTML = `
      <tr>
        <th class="compare-row-header">Attribute</th>
        ${methods.map(m => `
          <th style="width: 30%;">
            <div class="fw-bold fs-5">${m.name}</div>
            <span class="badge badge-${m.category} text-capitalize">${m.category}</span>
          </th>
        `).join('')}
      </tr>
    `;

    const rows = [
      { label: "Description", fn: m => `<p class="small mb-0">${m.description}</p>` },
      { label: "Best Used When", fn: m => `<p class="small mb-0">${m.best_used_when}</p>` },
      { label: "Sample Size Guidance", fn: m => `<span class="small fw-semibold text-primary">${m.sample_size_guidance}</span>` },
      { label: "Time Required", fn: m => `<span class="badge bg-light text-dark border text-capitalize">${m.time_required}</span>` },
      { label: "Resource Cost", fn: m => `<span class="badge bg-light text-dark border text-capitalize">${m.cost}</span>` },
      { label: "Key Strengths", fn: m => `<ul class="small mb-0 ps-3">${(m.strengths || []).map(s => `<li>${s}</li>`).join('')}</ul>` },
      { label: "Limitations", fn: m => `<ul class="small mb-0 ps-3">${(m.limitations || []).map(l => `<li>${l}</li>`).join('')}</ul>` },
      { label: "Data Collection", fn: m => `<div class="d-flex flex-wrap gap-1">${(m.typical_data_collection || []).map(t => `<span class="pill-tag">${t}</span>`).join('')}</div>` },
      { label: "Analysis Tools", fn: m => `<div class="d-flex flex-wrap gap-1">${(m.typical_analysis_techniques || []).map(t => `<span class="pill-tag">${t}</span>`).join('')}</div>` },
      { label: "Ethics Considerations", fn: m => `<p class="small text-muted mb-0">${m.ethical_considerations}</p>` },
    ];

    document.getElementById('compareBody').innerHTML = rows.map(r => `
      <tr>
        <td class="compare-row-header small">${r.label}</td>
        ${methods.map(m => `<td>${r.fn(m)}</td>`).join('')}
      </tr>
    `).join('');
  }

  populateSelects();
  renderCompare();
</script>
"""
with open(os.path.join(DOCS_DIR, "compare.html"), "w", encoding="utf-8") as f:
    f.write(make_page("Compare Methodologies", compare_content, active="compare", extra_scripts=compare_script))

# 4. RULES.HTML
rules_content = """
<div class="d-flex flex-wrap justify-content-between align-items-center mb-4">
  <div>
    <h2 class="fw-bold mb-1"><i class="bi bi-sliders text-primary me-2"></i>Declarative Rules Catalog</h2>
    <p class="text-muted mb-0">Browse all 66 transparent expert rules applied by the scoring engine with textbook justifications.</p>
  </div>
  <a href="questionnaire.html" class="btn btn-primary mt-3 mt-md-0">
    <i class="bi bi-play-circle me-1"></i> Test in Questionnaire
  </a>
</div>

<div class="filter-bar mb-4">
  <div class="row g-3 align-items-center">
    <div class="col-md-7">
      <div class="d-flex flex-wrap gap-2 align-items-center" id="ruleFilters">
        <span class="text-muted small fw-semibold me-2">Effect:</span>
        <button class="btn btn-sm btn-primary rounded-pill rule-filter" data-effect="all">All (66)</button>
        <button class="btn btn-sm btn-outline-success rounded-pill rule-filter" data-effect="boost">Boosts</button>
        <button class="btn btn-sm btn-outline-warning text-dark rounded-pill rule-filter" data-effect="penalty">Penalties</button>
        <button class="btn btn-sm btn-outline-danger rounded-pill rule-filter" data-effect="hard_exclude">Hard Excludes</button>
      </div>
    </div>
    <div class="col-md-5">
      <div class="input-group">
        <span class="input-group-text bg-white"><i class="bi bi-search text-muted"></i></span>
        <input type="text" id="ruleSearch" class="form-control" placeholder="Search rule ID, method, or reason...">
      </div>
    </div>
  </div>
</div>

<div class="custom-card overflow-hidden">
  <div class="table-responsive">
    <table class="table table-hover align-middle mb-0">
      <thead class="table-light">
        <tr>
          <th style="width: 180px;">Rule ID</th>
          <th style="width: 160px;">Target Method</th>
          <th style="width: 140px;">Effect & Weight</th>
          <th>Matched Conditions</th>
          <th>Academic Reason & Rationale</th>
        </tr>
      </thead>
      <tbody id="rulesTableBody"></tbody>
    </table>
  </div>
</div>
"""

rules_script = """
<script>
  let ruleEffect = 'all';
  let ruleSearchTerm = '';

  function renderRules() {
    const tbody = document.getElementById('rulesTableBody');
    const filtered = RULES_DATA.filter(r => {
      if (ruleEffect !== 'all' && (r.effect || 'boost') !== ruleEffect) return false;
      if (ruleSearchTerm) {
        const s = ruleSearchTerm.toLowerCase();
        const idMatch = (r.id || '').toLowerCase().includes(s);
        const mMatch = (r.method_id || '').toLowerCase().includes(s);
        const rMatch = (r.reason_text || '').toLowerCase().includes(s);
        if (!idMatch && !mMatch && !rMatch) return false;
      }
      return true;
    });

    if (filtered.length === 0) {
      tbody.innerHTML = `<tr><td colspan="5" class="text-center py-5 text-muted">No rules match your search criteria.</td></tr>`;
      return;
    }

    tbody.innerHTML = filtered.map(r => `
      <tr>
        <td><span class="font-monospace small fw-bold text-dark">${r.id}</span></td>
        <td><span class="badge bg-light text-primary border">${r.method_id}</span></td>
        <td>
          ${r.effect === 'boost' ? `<span class="badge bg-success bg-opacity-10 text-success border border-success border-opacity-25">+${Math.round(r.weight)} pts</span>` :
            r.effect === 'penalty' ? `<span class="badge bg-warning bg-opacity-10 text-warning border border-warning border-opacity-25">-${Math.round(r.weight)} pts</span>` :
            `<span class="badge bg-danger bg-opacity-10 text-danger border border-danger border-opacity-25">Hard Exclude</span>`}
        </td>
        <td>
          <div class="d-flex flex-wrap gap-1">
            ${Object.entries(r.conditions || {}).map(([k, v]) => `
              <span class="badge bg-light text-dark border small" style="font-size:0.75rem;">
                <span class="text-muted">${k}:</span> ${v}
              </span>
            `).join('')}
          </div>
        </td>
        <td><div class="small text-muted">${r.reason_text}</div></td>
      </tr>
    `).join('');
  }

  document.querySelectorAll('.rule-filter').forEach(btn => {
    btn.addEventListener('click', (e) => {
      document.querySelectorAll('.rule-filter').forEach(b => {
        b.className = 'btn btn-sm rounded-pill rule-filter ' + (b === e.target ? 'btn-primary' : 'btn-outline-secondary');
      });
      ruleEffect = e.target.getAttribute('data-effect');
      renderRules();
    });
  });

  document.getElementById('ruleSearch').addEventListener('input', (e) => {
    ruleSearchTerm = e.target.value.trim();
    renderRules();
  });

  renderRules();
</script>
"""
with open(os.path.join(DOCS_DIR, "rules.html"), "w", encoding="utf-8") as f:
    f.write(make_page("Rules Catalog", rules_content, active="rules", extra_scripts=rules_script))

# 5. DASHBOARD.HTML
dashboard_content = """
<div class="d-flex flex-wrap justify-content-between align-items-center mb-4">
  <div>
    <h2 class="fw-bold mb-1"><i class="bi bi-graph-up text-primary me-2"></i>Empirical Validation Dashboard</h2>
    <p class="text-muted mb-0">Automated benchmark evaluation of the rule engine across 30 published academic scenarios.</p>
  </div>
  <a href="questionnaire.html" class="btn btn-primary mt-3 mt-md-0">
    <i class="bi bi-play-circle me-1"></i> Run Live Assessment
  </a>
</div>

<!-- KPI Cards -->
<div class="row g-3 mb-4">
  <div class="col-md-3">
    <div class="custom-card p-3 h-100 border-start border-4 border-success">
      <div class="text-muted small fw-semibold mb-1">Top-1 Benchmark Accuracy</div>
      <div class="d-flex align-items-baseline gap-2 mb-2">
        <span class="display-6 fw-bold text-success" id="top1Acc">--%</span>
        <span class="small text-muted" id="top1Count">(0/30)</span>
      </div>
      <div class="progress" style="height: 6px;">
        <div class="progress-bar bg-success" id="top1Bar" style="width: 0%;"></div>
      </div>
    </div>
  </div>

  <div class="col-md-3">
    <div class="custom-card p-3 h-100 border-start border-4 border-primary">
      <div class="text-muted small fw-semibold mb-1">Top-3 Benchmark Accuracy</div>
      <div class="d-flex align-items-baseline gap-2 mb-2">
        <span class="display-6 fw-bold text-primary" id="top3Acc">--%</span>
        <span class="small text-muted" id="top3Count">(0/30)</span>
      </div>
      <div class="progress" style="height: 6px;">
        <div class="progress-bar bg-primary" id="top3Bar" style="width: 0%;"></div>
      </div>
    </div>
  </div>

  <div class="col-md-3">
    <div class="custom-card p-3 h-100 border-start border-4 border-info">
      <div class="text-muted small fw-semibold mb-1">Total Benchmarks</div>
      <div class="d-flex align-items-baseline gap-2 mb-2">
        <span class="display-6 fw-bold text-info">30</span>
        <span class="small text-muted">Scenarios</span>
      </div>
      <div class="small text-muted">Creswell, Kothari, Yin</div>
    </div>
  </div>

  <div class="col-md-3">
    <div class="custom-card p-3 h-100 border-start border-4 border-warning">
      <div class="text-muted small fw-semibold mb-1">Rule Engine Ruleset</div>
      <div class="d-flex align-items-baseline gap-2 mb-2">
        <span class="display-6 fw-bold text-dark">66</span>
        <span class="small text-muted">Rules</span>
      </div>
      <div class="small text-muted">100% Deterministic</div>
    </div>
  </div>
</div>

<!-- Benchmarks Table -->
<div class="custom-card overflow-hidden">
  <div class="p-4 border-bottom bg-light">
    <h5 class="fw-bold mb-1"><i class="bi bi-shield-check text-success me-2"></i>30 Benchmark Scenario Verification Results</h5>
    <p class="text-muted small mb-0">Each case executes through the client-side rule engine against textbook gold standards.</p>
  </div>
  <div class="table-responsive">
    <table class="table table-hover align-middle mb-0">
      <thead class="table-light">
        <tr>
          <th style="width: 70px;">ID</th>
          <th>Scenario Title</th>
          <th>Domain</th>
          <th>Expected Gold-Standard</th>
          <th>Engine Recommendation</th>
          <th class="text-center" style="width: 130px;">Result</th>
        </tr>
      </thead>
      <tbody id="benchmarkRows"></tbody>
    </table>
  </div>
</div>
"""

dashboard_script = """
<script>
  function runDashboard() {
    const results = evaluateBenchmarks();
    document.getElementById('top1Acc').innerText = results.top1_accuracy + '%';
    document.getElementById('top1Count').innerText = `(${results.top1_matches}/${results.total})`;
    document.getElementById('top1Bar').style.width = results.top1_accuracy + '%';

    document.getElementById('top3Acc').innerText = results.top3_accuracy + '%';
    document.getElementById('top3Count').innerText = `(${results.top3_matches}/${results.total})`;
    document.getElementById('top3Bar').style.width = results.top3_accuracy + '%';

    const tbody = document.getElementById('benchmarkRows');
    tbody.innerHTML = results.scenario_results.map(s => `
      <tr>
        <td><span class="badge bg-light text-dark border">${s.scenario_id}</span></td>
        <td>
          <div class="fw-semibold text-dark">${s.title}</div>
          <div class="small text-muted">${s.rationale}</div>
        </td>
        <td><span class="badge bg-light text-secondary border text-capitalize">${s.domain}</span></td>
        <td>
          <div class="d-flex flex-wrap gap-1">
            ${s.expected_method_ids.map(mid => `<span class="badge bg-secondary bg-opacity-10 text-dark border">${mid}</span>`).join('')}
          </div>
        </td>
        <td>
          <div class="fw-semibold text-primary">${s.top1_recommended || 'None'}</div>
          <div class="small text-muted">Top 3: ${s.top3_recommended.join(', ')}</div>
        </td>
        <td class="text-center">
          ${s.is_top1_match ? `<span class="badge bg-success"><i class="bi bi-check-circle me-1"></i>Top-1 Match</span>` :
            s.is_top3_match ? `<span class="badge bg-info text-dark"><i class="bi bi-check me-1"></i>Top-3 Match</span>` :
            `<span class="badge bg-danger"><i class="bi bi-x me-1"></i>Mismatch</span>`}
        </td>
      </tr>
    `).join('');
  }

  runDashboard();
</script>
"""
with open(os.path.join(DOCS_DIR, "dashboard.html"), "w", encoding="utf-8") as f:
    f.write(make_page("Validation Dashboard", dashboard_content, active="dashboard", extra_scripts=dashboard_script))

# 6. QUESTIONNAIRE.HTML
questionnaire_content = """
<div class="row justify-content-center">
  <div class="col-lg-9 col-xl-8">
    
    <div class="text-center mb-4">
      <h2 class="fw-bold mb-1">Study Design Questionnaire</h2>
      <p class="text-muted">Answer questions across 11 methodological dimensions to receive instant rule-based recommendations.</p>
    </div>

    <!-- Stepper Indicator -->
    <div class="wizard-step-indicator mb-4">
      <div class="text-center">
        <div class="wizard-step-node active" id="node1">1</div>
        <div class="small fw-semibold mt-1">Core Goals</div>
      </div>
      <div class="text-center">
        <div class="wizard-step-node" id="node2">2</div>
        <div class="small fw-semibold mt-1">Resources</div>
      </div>
      <div class="text-center">
        <div class="wizard-step-node" id="node3">3</div>
        <div class="small fw-semibold mt-1">Context & Ethics</div>
      </div>
    </div>

    <!-- Form Wizard -->
    <form id="wizardForm" class="custom-card p-4 p-md-5">
      
      <!-- STEP 1 -->
      <div id="step1" class="wizard-pane">
        <h4 class="fw-bold mb-3 text-primary"><i class="bi bi-compass me-2"></i>Step 1: Core Research Goals</h4>
        <div class="row g-3 mb-4">
          <div class="col-md-7">
            <label class="form-label fw-semibold">Study Title / Topic</label>
            <input type="text" id="study_title" class="form-control" value="Impact of AI Feedback on Software Engineering Productivity" required>
          </div>
          <div class="col-md-5">
            <label class="form-label fw-semibold">Researcher Name</label>
            <input type="text" id="student_name" class="form-control" value="Akilesh Student">
          </div>
        </div>

        <div class="mb-4">
          <label class="form-label fw-semibold">1. Primary Research Objective</label>
          <div class="row g-2">
            <div class="col-md-6">
              <label class="custom-card p-3 d-block cursor-pointer"><input type="radio" name="research_objective" value="explore" class="form-check-input me-2"> <strong>Explore</strong><div class="small text-muted">Investigate emerging phenomena with little prior theory.</div></label>
            </div>
            <div class="col-md-6">
              <label class="custom-card p-3 d-block cursor-pointer"><input type="radio" name="research_objective" value="describe" class="form-check-input me-2"> <strong>Describe</strong><div class="small text-muted">Characterize frequencies, distributions, or characteristics.</div></label>
            </div>
            <div class="col-md-6">
              <label class="custom-card p-3 d-block cursor-pointer"><input type="radio" name="research_objective" value="explain_test_hypothesis" checked class="form-check-input me-2"> <strong>Explain / Test Hypothesis</strong><div class="small text-muted">Examine causal relationships and test specific hypotheses.</div></label>
            </div>
            <div class="col-md-6">
              <label class="custom-card p-3 d-block cursor-pointer"><input type="radio" name="research_objective" value="build_evaluate_artifact" class="form-check-input me-2"> <strong>Build & Evaluate Artifact</strong><div class="small text-muted">Develop and evaluate algorithms, software, or tools.</div></label>
            </div>
          </div>
        </div>

        <div class="mb-4">
          <label class="form-label fw-semibold">2. Type of Primary Evidence / Data</label>
          <div class="row g-2">
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="data_type" value="numerical" checked class="form-check-input me-2"> <strong>Numerical</strong></label></div>
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="data_type" value="textual_narrative" class="form-check-input me-2"> <strong>Textual / Narrative</strong></label></div>
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="data_type" value="both" class="form-check-input me-2"> <strong>Both (Mixed)</strong></label></div>
          </div>
        </div>

        <div class="mb-4">
          <label class="form-label fw-semibold">3. Researcher Control Over Variables & Environment</label>
          <div class="row g-2">
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="control_over_variables" value="full" checked class="form-check-input me-2"> <strong>Full Control</strong></label></div>
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="control_over_variables" value="partial" class="form-check-input me-2"> <strong>Partial Control</strong></label></div>
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="control_over_variables" value="none" class="form-check-input me-2"> <strong>None (Observational)</strong></label></div>
          </div>
        </div>

        <div class="text-end">
          <button type="button" class="btn btn-primary px-4" onclick="goToStep(2)">Next: Resources <i class="bi bi-arrow-right ms-1"></i></button>
        </div>
      </div>

      <!-- STEP 2 -->
      <div id="step2" class="wizard-pane d-none">
        <h4 class="fw-bold mb-3 text-primary"><i class="bi bi-hourglass-split me-2"></i>Step 2: Practical Resources</h4>
        
        <div class="mb-4">
          <label class="form-label fw-semibold">4. Accessible Participant / Sample Size</label>
          <div class="row g-2">
            <div class="col-md-3"><label class="custom-card p-3 d-block"><input type="radio" name="sample_size_available" value="under_10" class="form-check-input me-2"> Under 10</label></div>
            <div class="col-md-3"><label class="custom-card p-3 d-block"><input type="radio" name="sample_size_available" value="10_to_30" class="form-check-input me-2"> 10 to 30</label></div>
            <div class="col-md-3"><label class="custom-card p-3 d-block"><input type="radio" name="sample_size_available" value="30_to_100" checked class="form-check-input me-2"> 30 to 100</label></div>
            <div class="col-md-3"><label class="custom-card p-3 d-block"><input type="radio" name="sample_size_available" value="over_100" class="form-check-input me-2"> Over 100</label></div>
          </div>
        </div>

        <div class="mb-4">
          <label class="form-label fw-semibold">5. Available Time Horizon</label>
          <div class="row g-2">
            <div class="col-md-3"><label class="custom-card p-3 d-block"><input type="radio" name="time_available" value="under_1_month" class="form-check-input me-2"> &lt; 1 month</label></div>
            <div class="col-md-3"><label class="custom-card p-3 d-block"><input type="radio" name="time_available" value="1_to_3_months" class="form-check-input me-2"> 1-3 months</label></div>
            <div class="col-md-3"><label class="custom-card p-3 d-block"><input type="radio" name="time_available" value="3_to_6_months" checked class="form-check-input me-2"> 3-6 months</label></div>
            <div class="col-md-3"><label class="custom-card p-3 d-block"><input type="radio" name="time_available" value="over_6_months" class="form-check-input me-2"> &gt; 6 months</label></div>
          </div>
        </div>

        <div class="mb-4">
          <label class="form-label fw-semibold">6. Budget & Financial Resources</label>
          <div class="row g-2">
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="budget" value="low" class="form-check-input me-2"> Low / Nil</label></div>
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="budget" value="medium" checked class="form-check-input me-2"> Medium</label></div>
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="budget" value="high" class="form-check-input me-2"> High</label></div>
          </div>
        </div>

        <div class="d-flex justify-content-between">
          <button type="button" class="btn btn-outline-secondary" onclick="goToStep(1)"><i class="bi bi-arrow-left me-1"></i> Back</button>
          <button type="button" class="btn btn-primary px-4" onclick="goToStep(3)">Next: Context & Ethics <i class="bi bi-arrow-right ms-1"></i></button>
        </div>
      </div>

      <!-- STEP 3 -->
      <div id="step3" class="wizard-pane d-none">
        <h4 class="fw-bold mb-3 text-primary"><i class="bi bi-shield-lock me-2"></i>Step 3: Context & Ethics</h4>

        <div class="mb-4">
          <label class="form-label fw-semibold">7. Participant Access</label>
          <div class="row g-2">
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="participant_access" value="easy" checked class="form-check-input me-2"> Easy Direct Access</label></div>
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="participant_access" value="difficult" class="form-check-input me-2"> Difficult / Gated</label></div>
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="participant_access" value="none_secondary_only" class="form-check-input me-2"> Secondary Data Only</label></div>
          </div>
        </div>

        <div class="mb-4">
          <label class="form-label fw-semibold">8. Academic Domain</label>
          <select id="domain" class="form-select">
            <option value="engineering" selected>Engineering / Computer Science</option>
            <option value="management">Management / Business</option>
            <option value="education">Education</option>
            <option value="health">Health / Biomedical</option>
            <option value="social_science">Social Sciences</option>
            <option value="other">Other</option>
          </select>
        </div>

        <div class="mb-4">
          <label class="form-label fw-semibold">9. Ethical Sensitivity</label>
          <div class="row g-2">
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="ethical_sensitivity" value="low" checked class="form-check-input me-2"> Low</label></div>
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="ethical_sensitivity" value="medium" class="form-check-input me-2"> Medium</label></div>
            <div class="col-md-4"><label class="custom-card p-3 d-block"><input type="radio" name="ethical_sensitivity" value="high" class="form-check-input me-2"> High</label></div>
          </div>
        </div>

        <div class="d-flex justify-content-between">
          <button type="button" class="btn btn-outline-secondary" onclick="goToStep(2)"><i class="bi bi-arrow-left me-1"></i> Back</button>
          <button type="button" class="btn btn-success btn-lg px-4" onclick="submitAssessment()"><i class="bi bi-check2-circle me-1"></i> Calculate Recommendations</button>
        </div>
      </div>

    </form>

    <!-- RESULTS DISPLAY CONTAINER -->
    <div id="resultsContainer" class="d-none mt-5"></div>

  </div>
</div>
"""

questionnaire_script = """
<script>
  function goToStep(step) {
    [1, 2, 3].forEach(s => {
      document.getElementById('step' + s).classList.toggle('d-none', s !== step);
      const node = document.getElementById('node' + s);
      node.classList.toggle('active', s === step);
      node.classList.toggle('completed', s < step);
    });
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function submitAssessment() {
    const getVal = (name) => {
      const el = document.querySelector(`input[name="${name}"]:checked`);
      return el ? el.value : '';
    };

    const inputs = {
      study_title: document.getElementById('study_title').value,
      student_name: document.getElementById('student_name').value,
      research_objective: getVal('research_objective'),
      data_type: getVal('data_type'),
      control_over_variables: getVal('control_over_variables'),
      sample_size_available: getVal('sample_size_available'),
      time_available: getVal('time_available'),
      budget: getVal('budget'),
      participant_access: getVal('participant_access'),
      domain: document.getElementById('domain').value,
      ethical_sensitivity: getVal('ethical_sensitivity')
    };

    const result = runRecommendationEngine(inputs);
    displayResults(result);
  }

  function displayResults(res) {
    const container = document.getElementById('resultsContainer');
    container.classList.remove('d-none');

    let warningsHtml = '';
    if (res.general_warnings && res.general_warnings.length > 0) {
      warningsHtml = res.general_warnings.map(w => `
        <div class="alert alert-warning py-2 px-3 small mb-2 d-flex align-items-center">
          <i class="bi bi-exclamation-triangle-fill text-warning me-2 fs-5"></i>
          <div>${w}</div>
        </div>
      `).join('');
    }

    container.innerHTML = `
      <div class="custom-card p-4 p-md-5 mb-4">
        <div class="d-flex justify-content-between align-items-start mb-3">
          <div>
            <span class="badge bg-primary text-uppercase px-3 py-1 mb-2"><i class="bi bi-cpu-fill me-1"></i> Recommendation Report</span>
            <h3 class="fw-bold mb-1">${res.study_title}</h3>
            <span class="small text-muted"><i class="bi bi-person me-1"></i>Researcher: <strong>${res.student_name}</strong></span>
          </div>
          <button class="btn btn-outline-secondary btn-sm" onclick="window.print()"><i class="bi bi-printer me-1"></i> Print / PDF</button>
        </div>
        ${warningsHtml}
      </div>

      <div class="mb-4">
        <h4 class="fw-bold mb-3"><i class="bi bi-award-fill text-warning me-2"></i>Top 3 Recommended Methodologies</h4>
        <div class="row g-4">
          ${res.top_methods.map((m, idx) => `
            <div class="col-lg-4">
              <div class="custom-card p-4 h-100 d-flex flex-column border-top border-4 ${idx === 0 ? 'border-primary' : idx === 1 ? 'border-info' : 'border-secondary'}">
                <div class="d-flex justify-content-between align-items-center mb-2">
                  <span class="badge ${idx === 0 ? 'bg-primary' : idx === 1 ? 'bg-info text-dark' : 'bg-secondary'} rounded-pill px-3 py-1 fw-bold">Rank #${m.rank}</span>
                  <span class="badge badge-${m.category} text-capitalize">${m.category}</span>
                </div>
                <h4 class="fw-bold mb-2">${m.method_name}</h4>
                <div class="mb-3">
                  <div class="d-flex justify-content-between small mb-1">
                    <span>Suitability Match:</span>
                    <strong class="text-success">${m.match_percentage}%</strong>
                  </div>
                  <div class="match-progress">
                    <div class="h-100 ${m.match_percentage > 70 ? 'match-bar-high' : 'match-bar-med'}" style="width: ${m.match_percentage}%;"></div>
                  </div>
                </div>
                <p class="small text-muted mb-3">${m.description}</p>
                ${m.why_this_method && m.why_this_method.length > 0 ? `
                  <div class="bg-light p-2 rounded small mt-auto">
                    <span class="fw-semibold text-primary d-block mb-1"><i class="bi bi-check2-circle me-1"></i>Why Recommended:</span>
                    <ul class="mb-0 ps-3">
                      ${m.why_this_method.map(r => `<li>${r}</li>`).join('')}
                    </ul>
                  </div>
                ` : ''}
              </div>
            </div>
          `).join('')}
        </div>
      </div>

      <div class="text-center mt-4">
        <button class="btn btn-outline-primary" onclick="goToStep(1)">
          <i class="bi bi-arrow-counterclockwise me-1"></i> Modify Answers & Re-test
        </button>
      </div>
    `;

    container.scrollIntoView({ behavior: 'smooth' });
  }
</script>
"""
with open(os.path.join(DOCS_DIR, "questionnaire.html"), "w", encoding="utf-8") as f:
    f.write(make_page("Questionnaire", questionnaire_content, active="questionnaire", extra_scripts=questionnaire_script))

print("All HTML files generated in docs/ successfully!")

# Research Methodology Selection Assistant (MethodAssist)

An intelligent, rule-based expert decision support system built to assist academic students and researchers in selecting the most appropriate research methodologies for their thesis, capstone projects, and dissertations.

Featuring 100% transparent, deterministic scoring with textbook citations (Creswell, Kothari, Yin, Saunders) and peer faculty validation audits.

---

## 🌟 Key Features

1. **Deterministic Rule Engine (40+ Rules)**
   - No black-box machine learning or hallucinating LLMs.
   - Declarative `rules.yaml` computing boosts, penalties, and hard constraints across 11 methodological dimensions.
   - Transparent, explainable justification for every recommendation.

2. **Curated Academic Knowledge Base (20 Methodologies)**
   - Spans Quantitative (Surveys, Experiments, Quasi-experiments, Secondary Analysis), Qualitative (Case Study, Grounded Theory, Phenomenology, Ethnography, Narrative), and Mixed Methods (Convergent Parallel, Explanatory Sequential, Exploratory Sequential).
   - Side-by-side comparison matrix of up to 3 methods across sample sizes, ethics, time, and analysis tools.

3. **Multi-Step Study Design Questionnaire**
   - 3-step intuitive wizard capturing objective, data type, variable control, sample size, access, and ethics.
   - Instant calculation of Top 3 primary recommendations, viable alternatives, and disqualified methods.

4. **Faculty Review Queue & Feedback Loop**
   - Role-based workflow for faculty advisors to audit student recommendations in real-time.
   - Ability to approve, reject, or request revisions with constructive methodological comments and alternative method suggestions.

5. **Empirical Validation Dashboard (30 Gold-Standard Benchmarks)**
   - Automated benchmark test suite evaluating Top-1 and Top-3 recommendation accuracy across 30 literature-derived scenarios.
   - Real-time review metrics and one-click dataset export to CSV.

---

## 🛠️ Technology Stack

- **Backend**: Python 3, FastAPI, Uvicorn, SQLAlchemy, Pydantic
- **Database**: SQLite (ORM via SQLAlchemy)
- **Frontend**: HTML5, Jinja2 Templates, Bootstrap 5, Bootstrap Icons, Chart.js
- **Testing**: Pytest (Unit tests, route integration tests, and rule catalog validation)

---

## 🚀 Quick Start Guide

### 1. Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/Akilesh0619/RESEARCH-METHODOLOGY-SELECTION-ASSISTANT.git
cd RESEARCH-METHODOLOGY-SELECTION-ASSISTANT
pip install -r requirements.txt
```

### 2. Run Test Suite
Verify all unit and integration tests:
```bash
pytest
```

### 3. Start the Local Server
```bash
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
Open your browser and navigate to:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🌐 1-Click Free Cloud Deployment

This project includes pre-configured deployment blueprints (`render.yaml`, `Procfile`, `run.py`, `vercel.json`):

### Option A: Render (Recommended for FastAPI)
1. Go to [render.com](https://render.com) and log in with GitHub.
2. Click **New +** -> **Web Service**.
3. Select this repository: `Akilesh0619/RESEARCH-METHODOLOGY-SELECTION-ASSISTANT`.
4. Render automatically detects `render.yaml` or set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
5. Click **Create Web Service**. Your free live URL will be ready in 1-2 minutes!

### Option B: Railway / Koyeb
1. Connect your GitHub repository.
2. The included `Procfile` and `run.py` automatically start the application.

---


## 🔑 Demo Login Accounts

| Role | Username | Password | Access Scope |
|---|---|---|---|
| **Student** | `student` | `student123` | Questionnaire, Recommendation Reports, Knowledge Base |
| **Faculty** | `faculty` | `faculty123` | Faculty Review Queue, Session Audits, Method Overrides |
| **Admin** | `admin` | `admin123` | Validation Dashboard, Declarative Rules Catalog |

---

## 📂 Project Directory Structure

```text
├── app/
│   ├── database.py             # SQLite database engine & session maker
│   ├── main.py                 # FastAPI application, lifespan seeding, middleware
│   ├── models.py               # SQLAlchemy ORM models
│   ├── schemas.py              # Pydantic schemas
│   ├── routers/
│   │   ├── admin.py            # Declarative rules catalog browser
│   │   ├── auth.py             # Session authentication (login/logout)
│   │   ├── kb.py               # Knowledge base listing, details & compare
│   │   ├── questionnaire.py    # Study design questionnaire & results
│   │   └── review.py           # Faculty review queue & validation dashboard
│   ├── services/
│   │   ├── auth_service.py     # Password hashing & session token management
│   │   ├── engine_service.py   # Rule engine execution & session persistence
│   │   ├── kb_service.py       # Method catalog loader & search filters
│   │   └── validation_service.py# Benchmark runner & CSV exporter
│   ├── static/css/             # Modern CSS styling & design system
│   └── templates/              # Jinja2 HTML templates
├── data/
│   ├── benchmark_scenarios.yaml# 30 peer-reviewed benchmark research scenarios
│   ├── methods.yaml            # 20 curated methodology catalog
│   └── rules.yaml              # 40+ declarative expert rules
├── engine/
│   ├── rule_engine.py          # Core rule matching & ranking pipeline
│   └── scoring.py              # Normalized scoring algorithm & feasibility warnings
├── tests/                      # Pytest suite (28 passing tests)
├── pytest.ini
└── requirements.txt
```

---

## 📜 Academic References

- Creswell, J. W., & Creswell, J. D. (2018). *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches*. SAGE.
- Kothari, C. R. (2004). *Research Methodology: Methods and Techniques*. New Age International.
- Yin, R. K. (2018). *Case Study Research and Applications: Design and Methods*. SAGE.
- Saunders, M., Lewis, P., & Thornhill, A. (2019). *Research Methods for Business Students*. Pearson.

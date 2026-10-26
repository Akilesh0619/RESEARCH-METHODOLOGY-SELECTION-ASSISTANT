import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.database import engine, Base, get_db
from app.services import kb_service, auth_service, validation_service
from app.routers import kb, questionnaire, auth, review, admin

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables
    Base.metadata.create_all(bind=engine)
    # Seed knowledge base methods, demo users, and benchmark scenarios on startup
    with Session(engine) as db:
        seeded = kb_service.seed_methods_from_yaml(db)
        print(f"[STARTUP] Seeded/verified {seeded} research methodologies in Knowledge Base.")
        auth_service.seed_demo_users(db)
        print("[STARTUP] Seeded/verified demo user accounts (student, faculty, admin).")
        seeded_benchmarks = validation_service.seed_benchmark_scenarios(db)
        print(f"[STARTUP] Seeded/verified {seeded_benchmarks} benchmark validation scenarios.")
    yield


app = FastAPI(
    title="Research Methodology Selection Assistant",
    description="A rule-based expert system for academic research methodology recommendation with faculty validation.",
    version="1.0.0",
    lifespan=lifespan
)

# Static files
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Templates
templates = Jinja2Templates(directory=TEMPLATES_DIR)


# Middleware to resolve authenticated user from session token
@app.middleware("http")
async def user_session_middleware(request: Request, call_next):
    request.state.user = None
    token = request.cookies.get("session_token")
    if token:
        user_id = auth_service.get_user_id_from_token(token)
        if user_id:
            try:
                db_generator = app.dependency_overrides.get(get_db, get_db)()
                db = next(db_generator)
                try:
                    request.state.user = auth_service.get_user_from_db(db, user_id)
                finally:
                    try:
                        next(db_generator)
                    except StopIteration:
                        pass
            except Exception:
                pass
    response = await call_next(request)
    return response



# Home page
@app.get("/", response_class=HTMLResponse)
def home_view(request: Request):
    user = getattr(request.state, "user", None)
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={
            "active_page": "home",
            "user": user,
        }
    )


# Register Routers
app.include_router(auth.router)
app.include_router(kb.router)
app.include_router(questionnaire.router)
app.include_router(review.router)
app.include_router(admin.router)


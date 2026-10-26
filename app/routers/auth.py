import os
from typing import Optional
from fastapi import APIRouter, Depends, Request, Response, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.services import auth_service

router = APIRouter(prefix="/auth")

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "templates")
templates = Jinja2Templates(directory=TEMPLATES_DIR)


@router.get("/login", response_class=HTMLResponse)
def login_view(request: Request):
    user = getattr(request.state, "user", None)
    if user:
        return RedirectResponse(url="/", status_code=303)

    return templates.TemplateResponse(
        request=request,
        name="auth/login.html",
        context={
            "active_page": "login",
            "user": None,
        }
    )


@router.post("/login")
async def handle_login(
    request: Request,
    response: Response,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        (User.username == username.strip()) | (User.email == username.strip())
    ).first()

    if not user or not auth_service.verify_password(password.strip(), user.hashed_password):
        return templates.TemplateResponse(
            request=request,
            name="auth/login.html",
            context={
                "active_page": "login",
                "user": None,
                "error_message": "Invalid username or password. Please try the demo quick-fill credentials."
            },
            status_code=401
        )

    # Issue signed session cookie
    token = auth_service.create_session_token(user.id)
    redirect_target = "/review/queue" if user.role in ["faculty", "admin"] else "/questionnaire"
    redirect_resp = RedirectResponse(url=redirect_target, status_code=303)
    redirect_resp.set_cookie(
        key="session_token",
        value=token,
        httponly=True,
        max_age=86400 * 7,
        samesite="lax"
    )
    return redirect_resp


@router.get("/logout")
def handle_logout():
    resp = RedirectResponse(url="/", status_code=303)
    resp.delete_cookie(key="session_token")
    return resp

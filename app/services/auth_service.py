import hashlib
import hmac
import os
from typing import Optional
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from sqlalchemy.orm import Session
from app.models import User

SECRET_KEY = os.environ.get("SECRET_KEY", "methodassist-secret-salt-2026-key")
SESSION_SALT = "methodassist-session-salt"
serializer = URLSafeTimedSerializer(SECRET_KEY)


def hash_password(password: str) -> str:
    """Generates salted SHA-256 password hash."""
    salt = "methodassist_salt_v1"
    hashed = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        100000
    )
    return hashed.hex()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies plain password against stored hash."""
    return hmac.compare_digest(hash_password(plain_password), hashed_password)


def create_session_token(user_id: int) -> str:
    """Creates signed tamper-proof session token."""
    return serializer.dumps({"user_id": user_id}, salt=SESSION_SALT)


def get_user_id_from_token(token: str) -> Optional[int]:
    """Decodes and validates session token."""
    try:
        data = serializer.loads(token, salt=SESSION_SALT, max_age=86400 * 7)  # 7 days
        return data.get("user_id")
    except (BadSignature, SignatureExpired):
        return None


def seed_demo_users(db: Session):
    """Seeds student, faculty, and admin demo accounts if not already present."""
    demo_users = [
        {
            "username": "student",
            "email": "student@college.edu",
            "password": "student123",
            "role": "student",
            "full_name": "Akilesh Student",
            "department": "Computer Science & Engineering"
        },
        {
            "username": "faculty",
            "email": "faculty@college.edu",
            "password": "faculty123",
            "role": "faculty",
            "full_name": "Dr. Sarah Jenkins",
            "department": "Research Methodology Dept"
        },
        {
            "username": "admin",
            "email": "admin@college.edu",
            "password": "admin123",
            "role": "admin",
            "full_name": "Prof. Alan Vance",
            "department": "Academic Affairs & Dean of Research"
        }
    ]

    for u in demo_users:
        existing = db.query(User).filter(User.username == u["username"]).first()
        if not existing:
            new_user = User(
                username=u["username"],
                email=u["email"],
                hashed_password=hash_password(u["password"]),
                role=u["role"],
                full_name=u["full_name"],
                department=u["department"]
            )
            db.add(new_user)
    db.commit()


def get_user_from_db(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()

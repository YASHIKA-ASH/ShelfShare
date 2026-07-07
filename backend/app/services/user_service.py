from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password
from app.utils.security import verify_password


def create_user(db: Session, user: UserCreate):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise ValueError("Email already registered")

    db_user = User(
    full_name=user.full_name,
    email=user.email,
    password_hash=hash_password(user.password),
    phone=user.phone,
    role=user.role
)

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user


def authenticate_user(db: Session, email: str, password: str):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return None

    if not verify_password(
        password,
        user.password_hash
    ):
        return None

    return user
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin, Token
from app.services.user_service import authenticate_user
from app.utils.jwt import create_access_token

from app.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register", response_model=UserResponse)
def register_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    try:
        return create_user(db, user)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    
@router.post("/login", response_model=Token)
def login(
    user: UserLogin,
    db: Session = Depends(get_db)
):

    db_user = authenticate_user(
        db,
        user.email,
        user.password
    )

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={
            "sub": str(db_user.id)
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }    
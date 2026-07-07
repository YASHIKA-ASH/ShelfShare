from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.wishlist_service import get_wishlist
from app.dependencies import get_db
from app.services.wishlist_service import remove_wishlist
from app.services.wishlist_service import recommend_books
from app.schemas.wishlist import WishlistCreate
from app.services.wishlist_service import add_to_wishlist
from app.schemas.wishlist_response import WishlistResponse
router = APIRouter(
    prefix="/wishlist",
    tags=["Wishlist"]
)

@router.post(
    "/",
    response_model=WishlistResponse
)
def create_wishlist(
    wishlist: WishlistCreate,
    db: Session = Depends(get_db)
):

    current_user = Depends(get_current_user)

    return add_to_wishlist(
        db,
        current_user.id,
        wishlist
)

@router.get("/{user_id}")
def view_wishlist(
    user_id: int,
    db: Session = Depends(get_db)
):

    return get_wishlist(
        db,
        user_id
    )

@router.delete("/{wishlist_id}")
def delete_wishlist(
    wishlist_id: int,
    db: Session = Depends(get_db)
):

    return remove_wishlist(
        db,
        wishlist_id
    )

@router.get("/recommend/{user_id}")
def recommend(
    user_id: int,
    db: Session = Depends(get_db)
):

    return recommend_books(
        db,
        user_id
    )
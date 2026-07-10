from fastapi import FastAPI
from app.database import Base, engine
from app.routers.user import router as user_router
from app.models import User, Book
from app.routers.book import router as book_router
from app.models.book import Book
from app.routers.scan import router as scan_router
from app.models.rental import Rental
from app.routers.rental import router as rental_router
from app.models.wishlist import Wishlist
from app.routers.wishlist import router as wishlist_router
from app.routers.search import router as search_router
from app.routers.dashboard import router as dashboard_router
from app.models.book_copy import BookCopy
from app.routers.book_copy import router as book_copy_router
from app.models.reservation import Reservation
from app.routers.reservation import router as reservation_router
from app.models.payment import Payment
from app.routers.payment import router as payment_router
from fastapi.middleware.cors import CORSMiddleware



Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="ShelfShare API"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(book_copy_router)
app.include_router(dashboard_router)
app.include_router(user_router)
app.include_router(book_router)
app.include_router(rental_router)
app.include_router(wishlist_router)
app.include_router(search_router)
app.include_router(reservation_router)
app.include_router(payment_router)
@app.get("/")
def root():
    return {
        "message": "ShelfShare API Running"
    }
app.include_router(scan_router)
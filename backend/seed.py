from app.database import SessionLocal
from app.models.user import User
from app.models.book import Book
from app.models.book_copy import BookCopy
from app.models.wishlist import Wishlist
from app.models.reservation import Reservation
from app.models.rental import Rental

import uuid

db = SessionLocal()

# -----------------------
# Use existing user
# -----------------------

user = db.query(User).first()

if user is None:
    user = User(
        full_name="Demo User",
        email="demo@shelfshare.com",
        password_hash="demo123",
        phone="9876543210",
        role="Student"
    )
    db.add(user)
    db.commit()
    db.refresh(user)

print("Using User:", user.full_name)

# -----------------------
# Demo Books
# -----------------------

books = [
    {
        "title":"Database Management Systems",
        "author":"Raghu Ramakrishnan",
        "isbn":"9780072465631",
        "subject":"DBMS"
    },
    {
        "title":"Operating System Concepts",
        "author":"Abraham Silberschatz",
        "isbn":"9781119800361",
        "subject":"Operating Systems"
    },
    {
        "title":"Computer Networks",
        "author":"Andrew Tanenbaum",
        "isbn":"9780132126953",
        "subject":"Networks"
    },
    {
        "title":"Artificial Intelligence: A Modern Approach",
        "author":"Stuart Russell",
        "isbn":"9780134610993",
        "subject":"Artificial Intelligence"
    },
    {
        "title":"Digital Signal Processing",
        "author":"Oppenheim",
        "isbn":"9780131988422",
        "subject":"DSP"
    },
    {
        "title":"Python Crash Course",
        "author":"Eric Matthes",
        "isbn":"9781593279288",
        "subject":"Python"
    },
    {
        "title":"Data Structures and Algorithm Analysis",
        "author":"Mark Allen Weiss",
        "isbn":"9780132847377",
        "subject":"DSA"
    },
    {
        "title":"Computer Organization and Architecture",
        "author":"William Stallings",
        "isbn":"9780134101613",
        "subject":"COA"
    },
    {
        "title":"Network Security Essentials",
        "author":"William Stallings",
        "isbn":"9780134527338",
        "subject":"Security"
    },
    {
        "title":"Software Engineering",
        "author":"Ian Sommerville",
        "isbn":"9780137035151",
        "subject":"Software Engineering"
    }
]

saved_books = []

# -----------------------
# Add Books
# -----------------------

for b in books:

    existing = db.query(Book).filter(Book.isbn == b["isbn"]).first()

    if existing:
        saved_books.append(existing)
        continue

    book = Book(
        title=b["title"],
        author=b["author"],
        isbn=b["isbn"],
        publisher="Pearson",
        edition="Latest Edition",
        subject=b["subject"],
        branch="Computer Science",
        semester=5,
        description="Demo textbook for ShelfShare.",
        image_url="",
        owner_id=user.id
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    saved_books.append(book)

print("Books Added:", len(saved_books))

# -----------------------
# Add Copies
# -----------------------

for book in saved_books:

    existing = db.query(BookCopy).filter(BookCopy.book_id == book.id).count()

    if existing >= 3:
        continue

    for i in range(3):

        copy = BookCopy(

            book_id=book.id,

            barcode="BC-" + uuid.uuid4().hex[:10],

            rack=f"A{i+1}",

            condition="Good",

            status="Available"

        )

        db.add(copy)

db.commit()

print("Book Copies Added")

# -----------------------
# Wishlist
# -----------------------

for book in saved_books[:3]:

    exists = db.query(Wishlist).filter(
        Wishlist.user_id == user.id,
        Wishlist.book_id == book.id
    ).first()

    if not exists:
        db.add(
            Wishlist(
                user_id=user.id,
                book_id=book.id
            )
        )

db.commit()

print("Wishlist Added")

# -----------------------
# Reservations
# -----------------------

for book in saved_books[3:5]:

    exists = db.query(Reservation).filter(
        Reservation.user_id == user.id,
        Reservation.book_id == book.id
    ).first()

    if not exists:
        db.add(
            Reservation(
    user_id=user.id,
    book_id=book.id,
    queue_position=1,
    status="Waiting"
)
        )
db.commit()

print("Reservations Added")

# -----------------------
# Borrowed Books
# -----------------------

copies = db.query(BookCopy).limit(2).all()

for copy in copies:

    copy.status = "Borrowed"

    exists = db.query(Rental).filter(
        Rental.copy_id == copy.id
    ).first()

    if not exists:
        db.add(
            Rental(
                user_id=user.id,
                copy_id=copy.id
            )
        )

db.commit()

print("Borrowed Books Added")

print("\nSeed Completed Successfully!")
from app.ai.google_books import search_google_books

data = search_google_books(
    "Operating System Concepts",
    "Galvin"
)

print(data)
from app.ai.ocr import extract_text

text = extract_text(
    "uploads/book_images/book_cover.webp"
)

print(text)
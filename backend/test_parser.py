from app.ai.ocr import extract_text

from app.ai.parser import extract_book_details


text = extract_text(

    "uploads/book_images/book_cover.webp"

)

details = extract_book_details(text)

print(details)
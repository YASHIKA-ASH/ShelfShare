from app.ai.ocr import extract_text
from app.ai.llm import extract_metadata

image_path = "uploads/book_images/book_cover.webp"

ocr_text = extract_text(image_path)

print("========= OCR OUTPUT =========")
print(ocr_text)

print()

print("========= GEMINI OUTPUT =========")

result = extract_metadata(ocr_text)

print(result)
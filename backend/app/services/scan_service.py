import os
import shutil

from app.ai.ocr import extract_text
from app.ai.llm import extract_metadata


def scan_book(file):

    upload_folder = "uploads/book_images"

    os.makedirs(upload_folder, exist_ok=True)

    file_path = os.path.join(
        upload_folder,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print("Saved Image:", file_path)

    text = extract_text(file_path)

    print("OCR OUTPUT:\n")
    print(text)

    metadata = extract_metadata(text)

    print("AI OUTPUT:\n")
    print(metadata)

    return metadata
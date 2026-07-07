import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_metadata(ocr_text: str):

    prompt = f"""
You are an expert librarian.

Extract the following fields from this OCR text.

Return ONLY valid JSON.

Fields:
- title
- authors
- publisher
- edition
- subject

OCR Text:

{ocr_text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    cleaned = response.text.replace("```json", "").replace("```", "").strip()

    return json.loads(cleaned)
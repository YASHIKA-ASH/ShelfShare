import os
import json
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_metadata(image_path: str):

    with open(image_path, "rb") as f:
        image_bytes = f.read()

    prompt = """
You are an expert librarian.

Analyze this textbook cover image carefully.

Extract ONLY the following fields.

Return ONLY valid JSON.

{
    "title":"",
    "authors":[],
    "publisher":"",
    "edition":"",
    "subject":"",
    "isbn":"",
    "description":""
}

If any field is missing, return an empty string.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            prompt,
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/jpeg"
            )
        ]
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)
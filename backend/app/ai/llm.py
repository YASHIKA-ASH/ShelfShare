import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def extract_metadata(image_path: str):

    with open(image_path, "rb") as f:
        image_bytes = f.read()

    prompt = """
You are an expert librarian.

Analyze this textbook cover image.

Extract the following fields.

Return ONLY valid JSON.

{
    "title":"",
    "authors":[],
    "publisher":"",
    "edition":"",
    "subject":""
}

If a field is not visible, return an empty string.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            prompt,
            {
                "mime_type": "image/jpeg",
                "data": image_bytes
            }
        ]
    )

    cleaned = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(cleaned)
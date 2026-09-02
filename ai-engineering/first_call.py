import os
import httpx
from google import genai
from google.genai import errors, types
from pydantic import BaseModel

class Answer(BaseModel):
    summary: str # a text box
    confidence: float # a number box

# initialize the client with the API key from your environment
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not set")

client = genai.Client(api_key=api_key,
        http_options=types.HttpOptions(timeout=30000) # 30 seconds
        )

# USE A VALID AND CURRENT GEMINI MODEL IDENTIFIER
try:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Summarize this lab finding and rate your confidence 0-1: 'WBC count 14,000/uL, patient reports fever for 3 days'",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Answer)
        )
    
    print("Raw text:", response.text)
    print("Parsed:", response.parsed)
    print("Type of parsed:", type(response.parsed))
except errors.APIError as e:
    print(f"API call failed: {e}")
except httpx.TimeoutException as e:
    print(f"Request timed out: {e}")
except httpx.ConnectError as e:
    print(f"Could not connect - please check your network: {e}")

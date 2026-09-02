# a command-line tool that takes messy lab report text and extracts the test values into clean structured JSON:
# test_name, value, unit)

# import libraries
import os
import httpx
from google import genai
from google.genai import errors, types
from pydantic import BaseModel
from typing import List

class LabValue(BaseModel):
    test_name: str
    value: str
    unit: str

class LabReport(BaseModel):
    lab_values: List[LabValue]
    clinical_interpretation: str
    confidence: float

# initializing client with api key
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key: # creating a check for api key.
    raise ValueError("GOOGLE_API_KEY not set. Kindly set it and continue")

client = genai.Client(api_key=api_key,
        http_options=types.HttpOptions(timeout=60000) # wait 10 seconds before giving up on the call
        )

# using gemini-3.6-flash to create a structured JSON response that follow the blue print of Answer class
try:
    response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents="""Extract every lab test value from this report:WBC 14,000/uL (high), HGB 13.2 g/dL, Platelets 250,000/uL, Temp 38.5c, patient febrile x3 days. Consider standardization of lab reporting and obey accrodingly.""",
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=LabReport
            )
        )
    for lab in response.parsed.lab_values:
        print(lab.test_name, lab.value, lab.unit)
except errors.APIError as e:
    print(f"API call failed: {e}")
except httpx.TimeoutException as e:
    print(f"Request timed out: {e}")
except httpx.ConnectError as e:
    print(f"could not connect. Check your network: {e}")

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
        http_options=types.HttpOptions(timeout=60000) # wait 60 seconds before giving up on the call
        )

# using gemini-3.6-flash to create a structured JSON response that follow the blue print of LabReport class
try:
    response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents="""Extract every lab test value from this report:WBC 14,000/uL (high), HGB 13.2 g/dL, Platelets 250,000/uL, Temp 38.5c, patient febrile x3 days, ESR 100 mmfall/hr. Consider standardization of lab reporting and obey accrodingly.""",
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=LabReport
            )
        )
    for lab in response.parsed.lab_values:
        print(lab.test_name, lab.value, lab.unit)
    print(f"Interpretation: {response.parsed.clinical_interpretation}")
    print(f"Confidence rate: {response.parsed.confidence}")

    #cost tracking
    usage = response.usage_metadata
    input_tokens = usage.prompt_token_count # prompt_token_count = number of texts in a prompt
    output_tokens = usage.candidates_token_count # output_tokens = number of texts in a response given by model
    # output_tokens are priced higher than input_tokens hence output cost than input cost
    input_cost = (input_tokens / 1_000_000) * 1.50
    output_cost = (output_tokens / 1_000_000) * 7.50
    total_cost = input_cost + output_cost
    print(f"Input tokens: {input_tokens}, Output tokens: {output_tokens}")
    print(f"Input cost = ${input_cost}, Output cost = ${output_cost}. Therefore Total Cost = ${total_cost:.6f}")

except errors.APIError as e:
    print(f"API call failed: {e}")
except httpx.TimeoutException as e:
    print(f"Request timed out: {e}")
except httpx.ConnectError as e:
    print(f"could not connect. Check your network: {e}")

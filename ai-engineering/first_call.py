import os
from google import genai

# initialize the client with the API key from your environment
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))

# USE A VALID AND CURRENT GEMINI MODEL IDENTIFIER
response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Explain artificial intelligence with respect to ai engineering in one short sentence."
        )
print(response.text)

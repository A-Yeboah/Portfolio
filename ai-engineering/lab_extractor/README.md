# Lab Value Extractor

## What it does
Extracts messy lab results and present a clean formatted results with regards to standardization.
Presents the final output with clinical interpretation and confidence rate.

## Why I built it
Lab results can sometimes be messy and hard to interprate for an entry level practitioner.
The application solves this by giving a confirmation of the interpretation a clinician may supposed.

## How to run it
1. Clone the repo and navigate to 'ai-engineering/lab_extractor/'
2. Create a virtual environment:
'''bash
python -m venv venv
source venv/bin/activate
3. Install dependencies:
'''bash
pip install google-genai pydantic httpx
4. Set your API key:
'''bash
export GOOGLE_API_KEY="your-key-here"
5. Run it:
'''bash
python3 lab_extractor.py

## What broke and what I learned
- Started with 'gemini-2.5-flash', which was deprecated mid-project - learned to always check for the current model namerather than trusting cached knowledge.
- First prompt said "summarize," which quietly turned exact values like "14,000/uL" into vague words like "elevated" - learned the difference between extraction and summarization prompts, and that models will happily paraphrase numbers unless explicitly told not to.
- Accidentally committed a virtual environment to git; '.gitignore' only stops future tracking, so cleaning up history that already had it required 'git filter-repo', not just adding a '.gitignore' entry.

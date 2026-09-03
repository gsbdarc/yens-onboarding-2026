import os

# This job only makes API calls — it does no heavy math — so keep number-crunching
# libraries (numpy/OpenBLAS via pandas) from spinning up a thread per core on the
# shared node. Must be set before pandas is imported.
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
os.environ.setdefault("OMP_NUM_THREADS", "1")

import json
import requests
import pandas as pd
import anthropic
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

# load_dotenv() puts ANTHROPIC_API_KEY from .env into the environment, which is where
# the client looks for it by default — so the key never appears in this file.
load_dotenv()
client = anthropic.Anthropic()

CSV_PATH = "data/aws_links.csv"
RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

# How many filings to process. Kept small on purpose: every filing is a paid API
# call, so a stray run shouldn't fire hundreds.
NUM_FILINGS = 10


class Form3Filing(BaseModel):
    insider_name: str
    insider_role: List[str]
    company_name: str
    company_cik: str
    filing_date: str


system_prompt = """
You are a data extraction agent for SEC Form 3 filings.

Extract the following fields:
- insider_name: The name of the insider (from reportingOwner or anywhere in the document).
- insider_role: A list of roles the insider holds (Director, Officer, 10% Owner, Other).
- company_name: The issuer's company name.
- company_cik: The CIK number of the issuer (from issuerCik or COMPANY DATA).
- filing_date: The filing date (prefer signatureDate or FILED AS OF DATE).

Return a SINGLE JSON object, not a list. Do not wrap it in an array.
"""

df = pd.read_csv(CSV_PATH)
# Skip the first row which is just the S3 folder URL
urls = df["urls"].dropna().tolist()
urls = [u for u in urls if u.endswith(".txt")]
urls = urls[:NUM_FILINGS]

total = len(urls)
print(f"Found {total} filings in {CSV_PATH}")

for idx, filing_url in enumerate(urls, 1):
    filename = filing_url.split("/")[-1]
    output_path = os.path.join(RESULTS_DIR, filename.replace(".txt", ".json"))

    print(f"[{idx}/{total}] Processing: {filename}")

    response = requests.get(filing_url)
    filing_text = response.text

    # output_format hands Form3Filing to the API as a schema the reply must match, so
    # .parsed_output comes back already validated against it.
    api_response = client.messages.parse(
        model="claude-haiku-4-5",
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": filing_text}],
        output_format=Form3Filing,
    )

    result = api_response.parsed_output
    if result is None:
        # No structured reply to save: the model declined, or the answer ran past
        # max_tokens before it was finished.
        raise RuntimeError(f"no output for {filename} ({api_response.stop_reason})")

    with open(output_path, "w") as f:
        json.dump(result.model_dump(), f, indent=2)

    print(f"  → saved {output_path}")

print(f"\nDone. {total} filings processed.")

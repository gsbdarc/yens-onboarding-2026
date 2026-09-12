"""Stage 3 of 3 — validates the model's answer against a schema.

This is the finished script. Day 2 profiles it and runs it under Slurm.

New since stage 2:
    Form3Filing            a Pydantic model declaring the fields you expect, and their types
    the schema in the prompt   so the model calls each field what your code calls it
    output_format          gives the API the Pydantic schema to generate and validate
    parsed_output          returns a validated Form3Filing object

Two other deliberate changes: it asks for more fields than stage 2 (the company and
the filing date), and it switches to a stronger model now that the prompt is settled.

To see exactly what changed:
    diff scripts/extract_form_3_step2_logged.py scripts/extract_form_3_one_file.py

Run it from the repo root:
    python3 scripts/extract_form_3_one_file.py
"""
import json
import logging
import os
from typing import List

import anthropic
from dotenv import load_dotenv
from pydantic import BaseModel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    handlers=[
        logging.FileHandler("form3_extract.log"),   # appends, so runs accumulate
        logging.StreamHandler(),                    # and still shows on screen
    ],
)
logger = logging.getLogger(__name__)

load_dotenv()   # reads .env from the repo root

# Filing to process. These ship in the repo; on the Yens you can point this at any
# Form 3 .txt file instead, e.g. a full EDGAR path under /zfs/data/NODR/EDGAR_HTTPS/.
FILING = "Cheniere_Energy_Inc"
FILING_PATH = f"data/sec_filings/{FILING}.txt"

MODEL = "claude-sonnet-5"   # stronger model, now that the prompt has settled
RESULTS_DIR = "results"
OUTPUT_PATH = f"{RESULTS_DIR}/form3_result.json"

client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY from the environment


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

Return one object matching the schema exactly.
"""

logger.info("Reading filing %s", FILING)
with open(FILING_PATH) as f:
    filing_text = f.read()

# No [:4000] slice here, unlike the earlier stages: these filings are only a few KB,
# and the fields above are spread through the whole document rather than bunched at
# the top. Keep the slice when the documents are long and the cost is real.
logger.info("Sending %d characters to %s", len(filing_text), MODEL)
response = client.messages.parse(
    model=MODEL,
    max_tokens=4096,
    thinking={"type": "disabled"},
    system=system_prompt,
    messages=[{"role": "user", "content": filing_text}],
    output_format=Form3Filing,
)
logger.info("Model responded")

raw = "".join(block.text for block in response.content if block.type == "text").strip()
result = response.parsed_output
if result is None:
    raise RuntimeError(f"No structured output returned (stop reason: {response.stop_reason})")

os.makedirs(RESULTS_DIR, exist_ok=True)

# messages.parse validates before returning. Keep the raw JSON text as an audit artifact,
# then save the normalized Pydantic representation used by the rest of the pipeline.
raw_path = f"{RESULTS_DIR}/form3_{FILING}.txt"
with open(raw_path, "w") as f:
    f.write(raw)
logger.info("Wrote %s", raw_path)

logger.info("Validated extraction for %s", result.company_name)

with open(OUTPUT_PATH, "w") as f:
    json.dump(result.model_dump(), f, indent=2)
logger.info("Wrote %s", OUTPUT_PATH)

print(json.dumps(result.model_dump(), indent=2))

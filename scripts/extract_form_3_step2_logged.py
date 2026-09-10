"""Stage 2 of 3 — adds logging, and saves the result to a file.

New since stage 1:
    logging       timestamped progress, to your screen AND to form3_extract.log
    FILING        the one value you change between runs, hoisted to the top
    an output file named after its input, so two runs leave two results

Everything else is the same as stage 1. To see exactly what changed:
    diff scripts/extract_form_3_step1_basic.py scripts/extract_form_3_step2_logged.py

Run it from the repo root:
    python3 scripts/extract_form_3_step2_logged.py
"""
import logging
import os

import anthropic
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    handlers=[
        logging.FileHandler("form3_extract.log"),   # appends, so runs accumulate
        logging.StreamHandler(),                    # and still shows on screen
    ],
)
logger = logging.getLogger(__name__)

load_dotenv()

FILING = "Cheniere_Energy_Inc"    # the one thing you change between runs
MODEL = "claude-haiku-4-5"
RESULTS_DIR = "results"

client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY from the environment

logger.info("Reading filing %s", FILING)
with open(f"data/sec_filings/{FILING}.txt") as f:
    filing_text = f.read()

logger.info("Sending %d characters to %s", len(filing_text[:4000]), MODEL)
response = client.messages.create(
    model=MODEL,
    max_tokens=256,
    system="You extract data from SEC filings. Be precise and concise.",
    messages=[
        {"role": "user", "content": f"Extract the insider's name and role.\nReply with only: NAME | ROLE\n\n{filing_text[:4000]}"},
    ],
)
logger.info("Model responded")

answer = "".join(block.text for block in response.content if block.type == "text").strip()
if not answer:
    raise RuntimeError(f"No text returned (stop reason: {response.stop_reason})")

os.makedirs(RESULTS_DIR, exist_ok=True)
output_path = f"{RESULTS_DIR}/form3_{FILING}.txt"    # output named after the input
with open(output_path, "w") as f:
    f.write(answer)
logger.info("Wrote %s", output_path)

print(answer)

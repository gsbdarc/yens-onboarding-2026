"""Stage 1 of 3 — the smallest thing that works.

Reads one SEC Form 3 filing, asks the model for the insider's name and role,
and prints the answer. That's it. Nothing here is written to disk.

What the next two stages add:
    Stage 2   logging, and saving the result to a file
    Stage 3   a Pydantic schema, so bad output fails loudly instead of quietly

Run it from the repo root:
    python3 scripts/extract_form_3_step1_basic.py
"""
import anthropic
from dotenv import load_dotenv

load_dotenv()   # reads .env from the repo root

FILING_PATH = "data/sec_filings/Cheniere_Energy_Inc.txt"
MODEL = "claude-haiku-4-5"   # fast and economical while the prompt is still changing

client = anthropic.Anthropic()   # reads ANTHROPIC_API_KEY from the environment

with open(FILING_PATH) as f:
    filing_text = f.read()

response = client.messages.create(
    model=MODEL,
    max_tokens=256,
    system="You extract data from SEC filings. Be precise and concise.",
    messages=[
        {"role": "user", "content": f"Extract the insider's name and role.\nReply with only: NAME | ROLE\n\n{filing_text[:4000]}"},
    ],
)

answer = "".join(block.text for block in response.content if block.type == "text").strip()
if not answer:
    raise RuntimeError(f"No text returned (stop reason: {response.stop_reason})")

print(answer)

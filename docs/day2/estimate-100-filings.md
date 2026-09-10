---
layout: default
title: "2. Estimate 100 Filings Resources"
parent: "Part 2 — Submit a Job Array"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 2
permalink: /day2/estimate-100-filings/
---

# Estimate 100 Filings Resources

{: .note }
> 🔴 **Red sticky** = I need help. Put it up the moment you are stuck — an instructor will
> come to you.
>
> 🟢 **Green sticky** = I have passed the checkpoint. Feel free to go back to the bonus
> exercises if you still have time, or help your table.

<svg viewBox="0 0 720 164" role="img" aria-labelledby="daymap-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:720px;height:auto;margin:1.5rem auto" font-family="'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="daymap-title">Day 2 arc — you are on step 5, scale (Part 2).</title>
  <defs>
    <marker id="daymap-ah" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c2cad4"/></marker>
  </defs>
  <text x="70" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">profile</text>
  <text x="210" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">document</text>
  <text x="350" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">submit</text>
  <text x="490" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">read logs</text>
  <text x="630" y="46" text-anchor="middle" font-size="17" font-weight="700" fill="#8C1515">scale (Part 2)</text>
  <line x1="92" y1="80" x2="608" y2="80" stroke="#c2cad4" stroke-width="3"/>
  <path d="M490,101 L490,124 Q490,130 484,130 L356,130 Q350,130 350,124 L350,103" fill="none" stroke="#c2cad4" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#daymap-ah)"/>
  <text x="420" y="150" text-anchor="middle" font-size="15" font-weight="400" fill="#6a7280">debug</text>
  <circle cx="70" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="70" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">1</text>
  <circle cx="210" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="210" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">2</text>
  <circle cx="350" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="350" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">3</text>
  <circle cx="490" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="490" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">4</text>
  <circle cx="630" cy="80" r="20" fill="#fff" stroke="#8C1515" stroke-width="3"/><text x="630" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8C1515">5</text>
</svg>

{: .note }
> Everything on this page runs from your clone, with the environment active:
>
> ```bash
> cd ~/yens-onboarding-2026
> source .venv/bin/activate
> ```

{: .important }
> **Task:** Estimate what a 100-filing array will need — **write the estimate down
> first** — then build it, run it, and check yourself against `sacct`.

Your job is to process and extract information from 100 SEC filings using a job array. The
filings are hosted online, and `data/aws_links.csv` — already in your cloned repo, alongside
`scripts/` and `slurm/` — provides the URLs of all of them.

You'll end up with two files: a new Python script that handles a single filing, and a Slurm
script to launch it as an array.

### 1. Estimate the resources — and write it down first

In Part 1 you measured the batch script over 10 filings and wrote three numbers into your
README. The temptation is to multiply them by ten. **Don't** — an array does not scale the
way a loop does, and working out which numbers move and which don't is the point of this
step.

What a `#SBATCH` directive asks for in an array is what **one task** gets, and one task here
handles **one filing**. So think about each resource separately:

- `--mem` and `--cpus-per-task` — sized for a single filing, whatever the array's length
- `--time` — also per task, so it covers one filing, not a hundred
- **wall-clock for the whole array** — not 100 × one filing, because the tasks run at the
  same time. How much less depends on how many actually get to run at once.

Reason it out, with Claude if you like:

```
> I'm turning a loop over 100 filings into a Slurm job array where each task handles one filing. Using my Profiling README (the 10-filing numbers), help me work out --mem, --cpus-per-task and --time per task, and how long the whole array should take.
```

**Before you submit anything**, write in your `README.md`: which resources **scale** with the
number of filings and which stay **flat** — and **why** — along with your per-task `--mem`,
`--cpus-per-task` and `--time`, and your guess at the wall-clock for the whole array.
Committing to a number *before* you run it is what makes the check at the end worth anything.

### 2. Build the array

**a. Figure out how to associate each task with a filing.**

{: .note }
> **Getting the task ID into Python** — the handover is spelled out on
> [1. Hello World Array]({{ '/day2/hello-world-array/' | relative_url }}). In the `.slurm`:
>
> ```bash
> python scripts/extract_array.py "$SLURM_ARRAY_TASK_ID"
> ```
>
> and `task_id = int(sys.argv[1])` on the Python side. Here that number runs `0` to `99`.

<details markdown="1">
<summary>💡 Hint — one way to do it</summary>

Every task runs the same script and differs only in its task ID, so the script can do the lookup itself — read the filings out of `data/aws_links.csv` and take the one matching this task:

```python
import sys
import pandas as pd

task_id = int(sys.argv[1])                      # handed over by the array script

# the CSV has a single `urls` column; drop any blank rows
urls = pd.read_csv("data/aws_links.csv")["urls"].dropna()

# keep only the filings themselves — the first row is the folder they live in,
# not a filing — and take the first 100
filings = [u for u in urls if u.endswith(".txt")][:100]

filing = filings[task_id]                       # task_id == 0 is the first filing
```

No shifting: the tasks are numbered from 0 and so is the list, so the task ID indexes it directly.

</details>

**b. Given a filing, write the usual extraction code.** Nothing new here — fetch the filing, send it to the API, validate the response with your Pydantic model. It's the same logic you wrote on Day 1 and looped over earlier today, except there's no loop: this task handles exactly one filing.

<details markdown="1">
<summary>💡 Hint — the extraction code, ready to copy</summary>

This is the script you wrote on Day 1, `scripts/extract_form_3_one_file.py`, with two changes.

It fetches the filing over the network rather than reading a fixed path off disk, since step **a** gives you a URL. And it calls Anthropic directly with `claude-haiku-4-5`, so the reply is validated against `Form3Filing` by the API instead of by you after the fact.

```python
import json
import os

import requests
import anthropic
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

load_dotenv()
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

Return a SINGLE JSON object, not a list. Do not wrap it in an array.
"""

# `filing` is the URL you picked in step a — fetch it over the network
filing_text = requests.get(filing).text

# output_format sends Form3Filing along as a schema the reply has to match
api_response = client.messages.parse(
    model="claude-haiku-4-5",
    max_tokens=4096,
    system=system_prompt,
    messages=[{"role": "user", "content": filing_text}],
    output_format=Form3Filing,
)

# already validated against the schema, so this is a Form3Filing instance
result = api_response.parsed_output
```

</details>

**c. Save the output to its own file,** so the result says what it came from and no two tasks write to the same place.

<details markdown="1">
<summary>💡 Hint — one way to do it</summary>

Name it after the filing, the way the batch script does — and then actually write it,
which is the step the other two hints leave you needing:

```python
from pathlib import Path

name = filing.split("/")[-1].replace(".txt", ".json")
output_path = Path("results") / name         # results/0000003570-22-000041.json
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(result.model_dump_json(indent=2))
```

With the three hints together you now have a runnable script: **a** picks the filing,
**b** extracts from it, and this writes the answer somewhere no other task will touch.

</details>

**d. Have the Slurm array script invoke your new Python script,** handing over the task ID as its argument:

```bash
python scripts/extract_array.py "$SLURM_ARRAY_TASK_ID"
```

{: .note }
> **Two things not to forget.** That line only works once the environment is ready, so the script still needs to `cd` to the repo root and activate the virtual environment first — the same two lines you wrote earlier. And the `#SBATCH --array=` directive has to be up with the other directives at the top — for 100 filings that is `#SBATCH --array=0-99`, since the tasks count from 0. Without it you've submitted one ordinary job, not an array, and `SLURM_ARRAY_TASK_ID` won't be set at all.

### 3. Size the directives from your estimate, then submit

Put the per-task numbers from step 1 into the `.slurm` — `--mem`, `--cpus-per-task` and
`--time` — alongside `--array=0-99`. You are asking Slurm for what you predicted, which is
what makes step 4 a real check rather than a formality.

`watch` re-runs a command every couple of seconds, so you can see the tasks start in
parallel and drop off as they finish:

```bash
mkdir -p logs
sbatch --reservation=class slurm/extract_array.slurm
watch squeue --me
```

The new thing to notice is the job IDs: an array shows up as many rows sharing one ID, with a task number after it — `12345678_0`, `12345678_1`, and so on — each moving through the same `PD` → `R` → gone lifecycle you watched in [3. Submit]({{ '/day2/submit-a-slurm-job/' | relative_url }}). Once it's done, check the per-task logs in `logs/` and the results in `results/`.

### 4. Check yourself against `sacct`

First, confirm the run actually did what you think it did:

```bash
ls results/*.json | wc -l        # should be 100
```

Then ask Slurm what the tasks really used. `MaxRSS` is peak memory and `Elapsed` is
wall-clock, per task:

```bash
sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS
```

Back in `README.md`, next to the estimate from step 1, write down the **actual** per-task
memory and time, the wall-clock for the whole array, and whether you **over- or
under-estimated** each one — and by how much. That comparison is the payoff; next time you
will size it better.

{: .note }
> **Where people are usually wrong.** Memory is normally over-asked by a lot, because a
> single filing is small. Wall-clock for the array is the interesting one: if you guessed
> close to a hundredth of the serial time you assumed every task ran at once, and if you
> guessed the full serial time you assumed none of them did. The truth sits between, set by
> how many tasks the scheduler let run concurrently.

<details markdown="1">
<summary>⭐ Bonus — combine the results into one CSV</summary>

The array leaves you a directory of JSON files, one per filing. For analysis you want a single table instead — one row per filing, one column per field.

Write a short script that reads every JSON in `results/` and writes them out as one CSV.

*Think before you type: what happens to a task that failed and never wrote a file?*

<details markdown="1">
<summary>Solution (expand after trying)</summary>

```python
# scripts/merge_results.py — combine the array's per-filing JSON into one CSV
import json
from pathlib import Path

import pandas as pd

RESULTS_DIR = Path("results")
OUTPUT_CSV = Path("results/extracted_filings.csv")

rows = []
for f in sorted(RESULTS_DIR.glob("*.json")):
    data = json.loads(f.read_text())
    data["filing"] = f.stem          # keep a record of which filing each row came from
    rows.append(data)

df = pd.DataFrame(rows)
df.to_csv(OUTPUT_CSV, index=False)

print(f"Wrote {len(df)} rows to {OUTPUT_CSV}")
```

A failed task simply left no file, so it never turns up in the glob and nothing crashes. That's also why the count matters: if `len(df)` is less than 100, some tasks didn't finish.

</details>

</details>

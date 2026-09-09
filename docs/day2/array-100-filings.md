---
layout: default
title: "2. Run 100 Filings Through an Array"
parent: "Part 2 — Submit a Job Array"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 2
permalink: /day2/array-100-filings/
---

# Run 100 Filings Through an Array

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put one up as soon as either is true — an instructor will come to you.

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

---

{: .important }
> **Task:** Process 100 SEC filings with a job array — one Python script that
> handles a single filing, plus a Slurm script that launches it 100 times.

Now over to you. Your job is the following: process and extract information from 100 SEC filings using a job array. The filings are hosted online, and `data/aws_links.csv` — already in your cloned repo, alongside `scripts/` and `slurm/` — provides the URLs of all of them for you to query.

You'll end up with two files: a new Python script that handles a single filing, and a Slurm script to launch it as an array — either a new one, or the `slurm/extract_form_3_batch.slurm` you wrote earlier today, adapted.

{: .note }
> **Use `claude-haiku-4-5` here, not a frontier model like Day 1's `gpt-5.2`.** Day 1's rule was *iterate cheap, then spend where it counts*. Here the arithmetic flips: the same call runs a hundred times, and cost and speed are now the thing you're managing. You get the cheaper, faster model in exchange for some accuracy, and handling that is part of the rest of today's work.

Work through it in four steps.

**1. Figure out how to associate each task with a filing.**

{: .note }
> **Getting the task ID into Python.** Slurm sets `SLURM_ARRAY_TASK_ID` in each task's environment. Your `.slurm` script passes it to your new Python script as a command-line argument:
>
> ```bash
> python scripts/extract_array.py "$SLURM_ARRAY_TASK_ID"
> ```
>
> and Python reads it back from `sys.argv` — a different number in every task:
>
> ```python
> import sys
>
> task_id = int(sys.argv[1])                      # 1, 2, … 100
> ```
>
> That's one way of doing it. The script could equally read the variable straight from its environment with `os.environ["SLURM_ARRAY_TASK_ID"]` and take no argument at all. Passing it in keeps the handover visible in the `.slurm`, and lets you run a single task by hand to test it.

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

filing = filings[task_id - 1]                   # task_id == 1 implies take the first filing
```

That `- 1` is the off-by-one from the warning above: the tasks count from 1, the list from 0.

</details>

**2. Given a filing, write the usual extraction code.** Nothing new here — fetch the filing, send it to the API, validate the response with your Pydantic model. It's the same logic you wrote on Day 1 and looped over earlier today, except there's no loop: this task handles exactly one filing.

<details markdown="1">
<summary>💡 Hint — the extraction code, ready to copy</summary>

This is the script you wrote on Day 1, `scripts/extract_form_3_one_file.py`, with two changes.

It fetches the filing over the network rather than reading a fixed path off disk, since step 1 gives you a URL. And it calls Anthropic directly with `claude-haiku-4-5`, so the reply is validated against `Form3Filing` by the API instead of by you after the fact.

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

# `filing` is the URL you picked in step 1 — fetch it over the network
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

**3. Save the output to its own file,** so the result says what it came from and no two tasks write to the same place.

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

With the three hints together you now have a runnable script: hint 1 picks the filing,
hint 2 extracts from it, and this writes the answer somewhere no other task will touch.

</details>

**4. Have the Slurm array script invoke your new Python script,** handing over the task ID as its argument:

```bash
python scripts/extract_array.py "$SLURM_ARRAY_TASK_ID"
```

{: .note }
> **Two things not to forget.** That line only works once the environment is ready, so the script still needs to `cd` to the repo root and activate the virtual environment first — the same two lines you wrote earlier. And the `#SBATCH --array=` directive has to be up with the other directives at the top: without it you've submitted one ordinary job, not an array, and `SLURM_ARRAY_TASK_ID` won't be set at all.

Then submit it and watch it run. `watch` re-runs a command every couple of seconds, so you can see the tasks start in parallel and drop off as they finish:

```bash
mkdir -p logs
sbatch --reservation=class_day2 slurm/extract_array.slurm
watch squeue --me
```

The new thing to notice is the job IDs: an array shows up as many rows sharing one ID, with a task number after it — `12345678_1`, `12345678_2`, and so on — each moving through the same `PD` → `R` → gone lifecycle you watched in [3. Submit]({{ '/day2/submit-a-slurm-job/' | relative_url }}). Once it's done, check the per-task logs in `logs/` and the results in `results/`.

---

<details markdown="1">
<summary>⭐ Bonus — if you finished early</summary>

**Bonus — Combine the results into one CSV**

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

---

**Bonus — Run all 992 filings**

`data/aws_links.csv` lists **992** filings. You have run 100. Scaling the array to all of
them is one number in one directive — except that it is not, and finding out why is the
exercise.

Try it and read the error:

```bash
sbatch --reservation=class_day2 --array=1-992 slurm/extract_array.slurm
```

Slurm refuses. The `normal` partition caps an array at **512 tasks**, and you can see the
ceiling yourself:

```bash
scontrol show config | grep MaxArraySize
```

So 992 filings cannot be 992 tasks. Two ways round it, and they are different tradeoffs:

- **Submit in batches.** Two arrays, `1-512` and `513-992`, with the second offset so its
  tasks index the right slice. Simple, and you can submit the second the moment the first
  drains.
- **Give each task more than one filing.** Keep the array small — say `1-100` — and have
  each task loop over ten filings, derived from its ID. Fewer, longer tasks; less
  scheduler overhead; and the per-task time limit now has to cover ten API calls, not one.

Whichever you pick, your rerun-safety check is what makes it survivable: a task that dies
partway through its ten leaves the finished ones on disk, and a resubmit only redoes what
is missing.

*Think before you run it: 992 paid API calls is real money. Work out the cost from your
10-filing timing first, and check the number with an instructor before submitting.*

---

## Before You Go

Run the [Part 2 Checkpoint]({{ '/day2/part2-checkpoint/' | relative_url }}) — four checks,
and two of them are just reading back what you wrote here.

You now have the full loop every real research pipeline needs:
**estimate → request → run → check → document.**

</details>

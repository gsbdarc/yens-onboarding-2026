---
layout: default
title: "Part 2 Lab"
parent: "Part 2 — Scale & Ship"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 1
permalink: /day2/part2-lab/
---

# Part 2 Lab

One script, one `--array` flag, every filing at once. Each task runs the same script and
gets a different task ID; that number is the only thing telling it which filing is its own.

Four exercises: prove an array fans out, run one over real work, make it safe to run twice,
then size a bigger run before you submit it.

{: .important }
> **Four mandatory exercises, about 55 minutes.** Exercise 1 takes two minutes and is worth
> doing even if you think you can skip it — it is the shortest possible version of the thing
> that goes wrong in exercise 2.
>
> Exercise 4 is the capstone, and it is the one to protect if you run short.

---

## 1. Watch an Array Fan Out

{: .important }
> **Mandatory.** **Task:** Submit `slurm/hello_array.slurm` unchanged, and confirm you got
> four tasks and four separate logs out of one submission.

The repo ships two scripts that differ by exactly one line. Read them both:

```bash
cd ~/yens-onboarding-2026
diff slurm/hello.slurm slurm/hello_array.slurm
```

The array version adds `#SBATCH --array=1-4` and changes its log paths from `%j` to
`%A_%a`. That is the whole difference between one job and four.

Submit it:

```bash
mkdir -p logs
sbatch --reservation=class_day2 slurm/hello_array.slurm
squeue --me
```

You get **one** job ID back, but `squeue` shows four rows — `12345678_1` through
`12345678_4`. When they finish:

```bash
cat logs/hello_*_*.out
```

Four files, four different task numbers. One submission, four independent tasks, four
logs that never collided.


<svg viewBox="0 0 618 270" role="img" aria-labelledby="array-title array-desc" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:616px;height:auto;margin:1.5rem auto" font-family="'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="array-title">One array script fans out into many tasks</title>
  <desc id="array-desc">A single submission script with the directive array equals 1 to N fans out into N independent tasks, numbered 1, 2, 3 and so on up to N. What each task does is determined by your code together with its array task ID.</desc>
  <!-- fan-out connectors (drawn first, behind boxes) -->
  <line x1="188" y1="129" x2="330" y2="37"  stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="188" y1="129" x2="330" y2="89"  stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="188" y1="129" x2="330" y2="141" stroke="#cbd3e0" stroke-width="1.5"/>
  <line x1="188" y1="129" x2="330" y2="221" stroke="#cbd3e0" stroke-width="1.5"/>
  <rect x="24" y="103" width="164" height="52" rx="10" fill="#eef1f8" stroke="#cdd4e6" stroke-width="1.5"/>
  <text x="106" y="124" font-size="12.5" font-weight="700" fill="#2c3e50" text-anchor="middle">Slurm script</text>
  <text x="106" y="142" font-size="10.5" fill="#6a7280" text-anchor="middle" font-family="'Source Code Pro', ui-monospace, SFMono-Regular, Menlo, monospace">--array=1–N</text>
  <rect x="330" y="15" width="264" height="44" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="462" y="31" font-size="12" fill="#2c3e50" text-anchor="middle">task 1</text>
  <text x="462" y="46" font-size="8" fill="#6a7280" text-anchor="middle">determined by your code <tspan font-weight="700">and</tspan> SLURM_ARRAY_TASK_ID</text>
  <rect x="330" y="67" width="264" height="44" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="462" y="83" font-size="12" fill="#2c3e50" text-anchor="middle">task 2</text>
  <text x="462" y="98" font-size="8" fill="#6a7280" text-anchor="middle">determined by your code <tspan font-weight="700">and</tspan> SLURM_ARRAY_TASK_ID</text>
  <rect x="330" y="119" width="264" height="44" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="462" y="135" font-size="12" fill="#2c3e50" text-anchor="middle">task 3</text>
  <text x="462" y="150" font-size="8" fill="#6a7280" text-anchor="middle">determined by your code <tspan font-weight="700">and</tspan> SLURM_ARRAY_TASK_ID</text>
  <text x="462" y="188" font-size="16" fill="#6b7280" text-anchor="middle">⋮</text>
  <rect x="330" y="199" width="264" height="44" rx="8" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="462" y="215" font-size="12" fill="#2c3e50" text-anchor="middle">task N</text>
  <text x="462" y="230" font-size="8" fill="#6a7280" text-anchor="middle">determined by your code <tspan font-weight="700">and</tspan> SLURM_ARRAY_TASK_ID</text>
  <!-- caption -->
  <text x="309" y="263" font-size="12.5" fill="#6a7280" text-anchor="middle">One submission becomes N independent tasks, each with its own task ID.</text>
</svg>

The task number is what makes this general. Every task runs the identical script, and `SLURM_ARRAY_TASK_ID` is the only thing that differs between them — so wherever the work needs to vary, you derive it from that number: which file to read, which row of a list to process, which parameter value to try.

{: .warning }
> **Counting from 1.** `--array=1-N` numbers the tasks 1, 2, … N. Slurm doesn't insist on that: numbering from 0 instead, so the tasks run 0 through N − 1, is equally valid. But starting at 1 is the convention used here, and it matters as soon as the task ID indexes something. In some languages a list of N items, `items`, is indexed 0 through N − 1, so a 1-based task ID has to be shifted — `items[task_id - 1]` rather than `items[task_id]`. Get it wrong and nothing complains up front: the first item is silently skipped, and the last task runs off the end of the list.
---

## 2. Run 100 Filings Through an Array

{: .important }
> **Mandatory.** **Task:** Process 100 SEC filings with a job array — one Python script that
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

The new thing to notice is the job IDs: an array shows up as many rows sharing one ID, with a task number after it — `12345678_1`, `12345678_2`, and so on — each moving through the same `PD` → `R` → gone lifecycle you watched in [Part 1 Lab]({{ '/day2/part1-lab/' | relative_url }}). Once it's done, check the per-task logs in `logs/` and the results in `results/`.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

---

## 3. Make Your Tasks Rerun-Safe

{: .important }
> **Mandatory.** **Task:** Make each array task skip work it has already done, then resubmit
> the same array and watch it finish in seconds.

A handful of your 100 will come back empty sooner or later — a node reboots, a task hits
its time limit, the API times out. Rerunning the whole array to catch them wastes compute
and, with a paid API, money.

Add the existence check to your script, then resubmit the array you just ran.

<details markdown="1">
<summary>💡 Hint — one way to do it</summary>

```python
# already done? skip — makes the array safe to resubmit after a partial failure
if output_path.exists():
    print(f"{output_path} already exists — skipping")
    sys.exit(0)
```

</details>

Nothing has been deleted, so every task should find its output and exit at once — the whole array finishing in seconds rather than minutes is the sign it worked.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

---

## 4. Capstone — Estimate, Submit, Compare

{: .important }
> **Mandatory.** **Task:** Estimate what a 100-filing run will cost in CPU, RAM, and time —
> **write the estimate down first** — then run it and check yourself against `sacct`.

All morning you have profiled and run **10 filings**. Scale to **100** — and commit to what
it will need *before* you run it.

### 1. Estimate the resources for 100 filings — and write it down first

You're running the same loop, just over 100 files instead of 10. Think about what **CPU**, **RAM**, and **time** it will take. Open `scripts/extract_form_3_batch.py` (or have Claude read it) and reason it out:

> Look at `scripts/extract_form_3_batch.py` and my Profiling README (the 10-filing numbers) and help me estimate the CPU, RAM, and wall-clock time this needs for 100 filings.

**Before you submit anything**, write in your `README.md`: which resources you think will **scale** with the number of filings processed and which will stay about flat — and **why** — along with your CPU, RAM, and wall-clock **estimate for 100**. Committing to a number *before* you run it is the whole point.


### 2. Write a Slurm script for the batch

You already built `slurm/extract_form_3_batch.slurm` for **10 filings**. Two changes:

1. In `scripts/extract_form_3_batch.py`, set `NUM_FILINGS = 100`.
2. In the `.slurm`, re-tune `--time`, `--mem` and `--cpus-per-task` to **your estimates for
   100**, and keep the email-notification lines so you get the completion summary.

{: .warning }
> **Confirm the edit took before you submit.** The filing count lives inside the Python
> script, not on the `sbatch` command line — so if the edit does not save, the job still
> succeeds and still emails you, having processed ten filings while holding a request
> sized for a hundred. Your "actuals" then describe the wrong run, and the honest
> conclusion is that you over-estimated by 10×.
>
> ```bash
> grep NUM_FILINGS scripts/extract_form_3_batch.py
> ```
>
> It should say `100`. Clear out the old results too, so what lands in `results/` is from
> this run only: `rm -f results/*.json`.


### 3. Submit and confirm it ran

{: .note }
> **Today only:** keep the class reservation flag — `--reservation=class_day2` — on your `sbatch` so the job runs on the reserved nodes. Drop it for your own work after today.

```bash
sbatch --reservation=class_day2 \
  slurm/extract_form_3_batch.slurm
squeue --me
```

Wait for the completion email. From it — and from
`sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS` — note **how long it took** and **how
much CPU and RAM it actually used** against what you requested.

Check you measured what you think you measured:

```bash
ls results/*.json | wc -l        # should be 100, not 10
```


### 4. Compare actual vs. your estimate

Back in `README.md`, next to the estimate you wrote in step 1, add the **actual** numbers from the email and `sacct`, and note whether you **over- or under-estimated** each resource — and by how much. That comparison is the payoff; next time you'll estimate better.


### 5. Commit and push from the Yens

Ask Claude Code to handle it:

> Add and commit `slurm/extract_form_3_batch.slurm` and my README changes with a message like "Day 2 Capstone: 100-filing batch", then push to my fork.


{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

---

---

## Bonus
{: .note }
> **Done with all four?** First check whether anyone at your table is stuck — explaining it is how it sticks. Then pick anything below.

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

---

## Before You Go

Run the [Part 2 Checkpoint]({{ '/day2/part2-checkpoint/' | relative_url }}) — four checks,
and two of them are just reading back what you wrote here.

You now have the full loop every real research pipeline needs:
**estimate → request → run → check → document.**

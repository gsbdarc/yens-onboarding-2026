---
layout: default
title: "2. Scale the Loop to an Array"
parent: "Part 2 — Submit a Job Array"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 2
permalink: /day2/loop-to-array/
---

# Scale the Loop to an Array

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
> **Task:** Turn Part 1's loop over filings into a job array that processes **100 filings**,
> get it running, then find out what it actually used. You write both files — there is
> nothing on this page to copy.

## What you already have

Three things, and putting them together is the exercise:

- **`scripts/extract_form_3_batch.py`** from Part 1 — Python that walks a list of filings,
  one API call at a time, waiting for each before starting the next.
- **The array from [1. Hello World Array]({{ '/day2/hello-world-array/' | relative_url }})** —
  one submission, many tasks, running the identical script. The only thing that differs
  between them is `SLURM_ARRAY_TASK_ID`, and that page also shows how that number gets into
  Python.
- **`data/aws_links.csv`** — already in your clone, with a `urls` column listing the filings.

You will end up writing two files: something in Python, and a `.slurm` to launch it. Working
out what each of them is responsible for is the part worth doing slowly.

{: .note }
> **Claude is fair game. Understanding is not optional.** Use it to draft, to debug, to
> explain an error you have not seen before. The one rule: you should be able to say what
> every line you keep is doing, and why. An array that works but that you cannot explain is
> worth less today than one that is broken and you can.

If you get stuck, there are hints at the bottom of this page — but try the reasoning first,
and ask the person next to you before you scroll.

## Before you submit

Write down what you think **one task** needs — `--mem`, `--cpus-per-task`, `--time`.
Anywhere is fine; a comment at the top of your `.slurm` is fine. You will compare it against
reality in a few minutes.

## Run it

`watch` re-runs a command every couple of seconds, so you can see the tasks start in
parallel and drop off as they finish:

```bash
mkdir -p logs
sbatch --reservation=class slurm/extract_array.slurm
watch squeue --me
```

The thing to notice is the job IDs: an array shows up as many rows sharing one ID, with a
task number after it — `12345678_0`, `12345678_1`, and so on — each moving through the same
`PD` → `R` → gone lifecycle you watched in
[3. Submit]({{ '/day2/submit-a-slurm-job/' | relative_url }}).

## What did it actually use?

First, confirm the run did what you think it did:

```bash
ls results/*.json | wc -l        # should be 100
```

Then ask Slurm what the tasks really used. `MaxRSS` is peak memory and `Elapsed` is
wall-clock, per task:

```bash
sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS
```

Compare that against the numbers you wrote down before submitting.

---

## Stuck?

Put up a **red sticky** and ask your table — someone near you has probably just hit the same
thing. If you want a nudge rather than an answer, these are in the order they usually help:

<details markdown="1">
<summary>💡 Hint 1 — what is different about task 7 and task 8?</summary>

Every task runs the *same* script. Nothing about the file changes between them; the only
thing Slurm hands each task that is unique is its task ID. So if the 100 tasks are to do 100
different things, the difference has to be derived from that number.

Ask yourself what the smallest useful unit of work is here. Part 1's script did 10 filings
in one process. What would one task doing *its share* look like — and what happens to the
loop if a task's share is a single filing?

</details>

<details markdown="1">
<summary>💡 Hint 2 — where the filings come from</summary>

`data/aws_links.csv` has one column, `urls`. Two things about it will bite you if you do not
look at the file first: not every row is a filing — the first one is the folder they live
in — and there are far more than 100 rows in it, so you need to take a slice.

Read it, look at it, and only then decide how a task picks its own row out.

</details>

<details markdown="1">
<summary>💡 Hint 3 — two tasks, one output file</summary>

All 100 tasks run the same code at roughly the same moment. If that code writes its answer
to a fixed path, you will finish with one file instead of 100, containing whichever task
happened to write last.

Whatever names the output has to be different in every task. You already have exactly one
thing that is guaranteed unique.

</details>

<details markdown="1">
<summary>💡 Hint 4 — the two that bite everyone</summary>

Neither of these is about your Python, and both produce confusing failures:

- **`#SBATCH --array=` has to sit with the other directives**, above the first real command.
  Below it, Slurm ignores it: you get one ordinary job, and `SLURM_ARRAY_TASK_ID` is never
  set. For 100 filings numbered from 0, that directive is `--array=0-99`.
- **A fresh shell on a compute node has no virtual environment.** Activating it in your
  terminal did nothing for the job. The `.slurm` has to `cd` to the repo and activate it
  itself — the same two lines you wrote in Part 1.

</details>

---

<details markdown="1">
<summary>⭐ Bonus — combine the results into one CSV</summary>

The array leaves you a directory of JSON files, one per filing. For analysis you want a
single table instead — one row per filing, one column per field.

Write a short script that reads every JSON in `results/` and writes them out as one CSV.

*Think before you type: what happens to a task that failed and never wrote a file? And what
does the row count tell you afterwards?*

</details>

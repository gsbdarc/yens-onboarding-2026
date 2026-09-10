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
> get it running, then find out what it actually used.

## What you already have

Nothing here is new. You have all three pieces already:

- **`scripts/extract_form_3_batch.py`** from Part 1 — Python that walks a list of filings,
  one API call at a time, waiting for each before starting the next.
- **The array from [1. Hello World Array]({{ '/day2/hello-world-array/' | relative_url }})** —
  one submission, many tasks, running the identical script. The only thing that differs
  between them is `SLURM_ARRAY_TASK_ID`, and that page also shows how that number gets into
  Python.
- **`data/aws_links.csv`** — already in your clone, with a `urls` column listing the filings.

You will end up writing two files: something in Python, and a `.slurm` to launch it.

{: .note }
> **Claude is fair game.** Use it to draft, to debug, to explain an error you have not seen
> before. The one rule: you should be able to say what every line you keep is doing, and why.
> An array that works but that you cannot explain is worth less today than one that is broken
> and you can.

If you get stuck, there are hints at the bottom of this page — but try the reasoning first,
and ask the person next to you before you scroll.

## Estimate, document, submit

The same flow as Part 1, so you already know how each step goes:

- **Estimate** what **one task** needs. Profile it the way you did this morning — but on one
  filing, not ten, because a `#SBATCH` directive sizes a single task, not the whole array.
- **Document** the numbers in your `README.md`, before you submit rather than after.
- **Submit**, with those numbers in the `.slurm`, and think about what the array directive
  has to say for 100 filings.

## Run it

Submit it, then watch it go. `watch` re-runs a command every couple of seconds, so you can
see the tasks start in parallel and drop off as they finish:

```bash
watch squeue --me
```

The thing to notice is the job IDs: an array shows up as many rows sharing one ID, with a
task number after it — `12345678_0`, `12345678_1`, and so on — each moving through the same
`PD` → `R` → gone lifecycle you watched in
[3. Submit]({{ '/day2/submit-a-slurm-job/' | relative_url }}).

## What did it actually use?

`MaxRSS` is peak memory and `Elapsed` is wall-clock, per task:

```bash
sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS
```

Compare that against what you estimated and wrote down. Over-asking for memory is the normal
result, and worth noticing.

---

## Stuck?

Put up a **red sticky** and ask your table — someone near you has probably just hit the same
thing. Nudges, roughly in the order they help:

<details markdown="1">
<summary>💡 Nothing changes but one number</summary>

Not the filing list, not the Python file. Every task runs the *identical* script, and the
only thing Slurm hands each one that is unique is its task ID. So if 100 tasks are to do 100
different things, the difference has to be derived from that number.

What is one task's share of 100 filings?

</details>

<details markdown="1">
<summary>💡 Test your Python interactively first</summary>

Run it by hand in a terminal, on one filing, before it goes anywhere near `sbatch`. You can
pass a task number in as an argument yourself to check it picks the right filing.

Debugging one script in front of you is quick. Debugging 100 queued copies through log files
is not.

</details>

<details markdown="1">
<summary>💡 Profile it, then size the job</summary>

Once it runs for one filing, time it and watch what it uses — the same way you profiled the
batch script this morning. Those are the numbers that go into `--mem`, `--cpus-per-task` and
`--time`, and they describe **one task**.

</details>

<details markdown="1">
<summary>💡 The array index</summary>

Did you start at 0 or at 1? Whichever you pick has to agree with how you index the filing
list, and Slurm will not warn you if it doesn't.

Get it wrong and nothing complains up front: you quietly skip one end of the list, and the
task at the other end runs off it.

</details>

<details markdown="1">
<summary>💡 How do you know it worked?</summary>

A job that finishes is not the same as a job that did the work. Two things to check, and
neither is `squeue`:

- the per-task `.err` files, for the tasks that failed
- the number of output files you ended up with, against the number you expected

</details>

### It ran, but something is off

Run down this list before asking — it is usually one of these:

- Did you create the log directory before submitting? Slurm will not make it for you, and a
  job whose `--output` path does not exist fails leaving nothing behind to explain why.
- Did you use `--reservation=class`? Without it you are queueing with everybody else.
- Did the `.slurm` `cd` to the repo and activate the virtual environment? A fresh shell on a
  compute node inherits neither.
- Is `#SBATCH --array=` up with the other directives, above the first real command? Below
  them it is ignored, you get one ordinary job, and `SLURM_ARRAY_TASK_ID` is never set.
- Does your script actually **write** its result, or only compute it?

---

<details markdown="1">
<summary>⭐ Bonus — combine the results into one CSV</summary>

The array leaves you a directory of JSON files, one per filing. For analysis you want a
single table instead — one row per filing, one column per field.

Have Claude write you a short script that reads every JSON and writes them out as one CSV,
then **document it as a step** in your README. It is part of your pipeline now, not a
one-off you ran once and forgot.

*Think before you type: what happens to a task that failed and never wrote a file? And what
does the row count tell you afterwards?*

**Going further.** Make the merge its own Slurm job, and have Slurm run it only if the array
finished cleanly:

```bash
sbatch --dependency=afterok:ARRAYJOBID slurm/merge_results.slurm
```

It sits in the queue as `PD` until the array succeeds, then runs on its own. If any task
fails, it never starts — which is what you want, rather than merging a half-finished
directory.

</details>

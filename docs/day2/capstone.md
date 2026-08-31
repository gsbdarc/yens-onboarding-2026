---
layout: default
title: "Day 2 Capstone"
parent: "Day 2 — The Cluster"
nav_order: 7
permalink: /day2/capstone/
---

# Day 2 Capstone

---

## The Capstone — Scale to 100 filings

{: .important }
> **Mandatory.** **Task:** Estimate what a 100-filing run will cost in CPU, RAM, and time —
> **write the estimate down first** — then run it and check yourself against `sacct`.

All day you've profiled and run **10 filings**. The capstone: scale to **100** — and **estimate what it needs *before* you run it**.

**Step back — what are we actually doing?** Each "filing" is a real **SEC Form 3**; your script hands it to the **Anthropic API**, which reads it and returns the structured fields. Scaling to 100 doesn't change that shape: the batch still walks the filings **one at a time**, making one blocking API call per filing and waiting for the answer before starting the next. That's why this job is **I/O-bound** — as you saw in profiling, the wall-clock time grows with the number of filings while RAM and CPU stay about flat.

### 1. Estimate the resources for 100 filings — and write it down first

You're running the same loop, just over 100 files instead of 10. Think about what **CPU**, **RAM**, and **time** it will take. Open `scripts/extract_form_3_batch.py` (or have Claude read it) and reason it out:

> Look at `scripts/extract_form_3_batch.py` and my Profiling README (the 10-filing numbers) and help me estimate the CPU, RAM, and wall-clock time this needs for 100 filings.

**Before you submit anything**, write in your `README.md`: which resources you think will **scale** with the number of filings processed and which will stay about flat — and **why** — along with your CPU, RAM, and wall-clock **estimate for 100**. Committing to a number *before* you run it is the whole point.

**Zoom out:** *the task hasn't changed — you're still sending each SEC Form 3 filing to the Anthropic API to extract its structured fields. There are just **100** of them now, processed one after another in a loop. You're sizing the resources for that loop.*

### 2. Write a Slurm script for the batch

You already built `slurm/extract_form_3_batch.slurm` for **10 filings** on the Slurm-job page. Now scale it: bump `NUM_FILINGS` to `100` in `scripts/extract_form_3_batch.py`, and re-tune `--time`, `--mem`, and `--cpus-per-task` in the `.slurm` with **your estimates for 100** (make sure the email-notification lines are there so you get a completion email).

**Zoom out:** *it's still one Python script with a big `for` loop — for each of the 100 Form 3 filings: read it, send it to the API, save the structured data. The Slurm script just runs that single script, once, on the cluster.*

### 3. Submit and confirm it ran

{: .note }
> **Today only:** keep the class reservation flag — `--reservation=class_day2` — on your `sbatch` so the job runs on the reserved nodes. Drop it for your own work after today.

```bash
sbatch --reservation=class_day2 \
  slurm/extract_form_3_batch.slurm
squeue --me
```

Wait for the completion email. From it — and from `sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS` — note **how long it took** and **how much CPU/RAM it actually used** versus what you requested.

**Zoom out:** *right now the cluster is working through 100 Form 3 filings, one API call at a time, pulling structured fields out of each.*

### 4. Compare actual vs. your estimate

Back in `README.md`, next to the estimate you wrote in step 1, add the **actual** numbers from the email and `sacct`, and note whether you **over- or under-estimated** each resource — and by how much. That comparison is the payoff; next time you'll estimate better.

**Zoom out:** *those numbers are the real cost of 100 sequential API calls extracting data from Form 3 filings — the actual work, now measured.*

### 5. Commit and push from the Yens

Ask Claude Code to handle it:

> Add and commit `slurm/extract_form_3_batch.slurm` and my README changes with a message like "Day 2 Capstone: 100-filing batch", then push to my fork.

**Zoom out:** *what you're saving is that pipeline — loop over Form 3 filings, extract structured data via the API — now proven at 100.*

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

---

## Finished Early?

**First, look around your table.** If anyone is still mid-capstone, help them — you have
just done the thing they are stuck on, and explaining it is how it sticks.

Then take your pick:

| Bonus | Where |
|---|---|
| The remaining `fix_me` puzzles — the highest-value bonus on the day, because reading a failed job's logs is the skill you need first | [Writing & Submitting a Slurm Job]({{ '/day2/slurm-job/#bonus' | relative_url }}) |
| Distill today's Slurm conventions into a reusable Claude skill | [Writing a Slurm Job with Claude]({{ '/day2/slurm-with-claude/' | relative_url }}) |
| Ask Slurm for a GPU and work out whether your job actually wanted one | [GPUs]({{ '/day2/gpus/' | relative_url }}) |
| Merge the array's per-filing JSON into one CSV | [Job Arrays]({{ '/day2/job-arrays/#bonus-combine-the-results-into-one-csv' | relative_url }}) |
| Local LLMs, LLM-as-a-judge, parallelization in depth, `scp` | [Reference]({{ '/reference/' | relative_url }}) |

{: .note }
> **Done?** Bring any lingering questions to the instructors — now is the time to ask.

---

## Day 2 — What You Learned

- **Compute environments** — CPU cores, RAM, and storage, and how laptop vs. Yens vs. cloud trade off.
- **Profiling** — measuring a script's time, CPU, and RAM with `time`, `userload`, and `htop`; telling **serial from parallel** and **CPU-bound from I/O-bound** work.
- **Slurm** — why a scheduler exists; reading the queue and partitions (`squeue`, `sinfo`, QoS caps).
- **Running jobs** — writing a Slurm script from scratch, submitting/monitoring/cancelling, reading `.out`/`.err` logs, and **debugging failed jobs** (code bug vs. OOM vs. timeout).
- **Job arrays** — one script, one `--array` flag, every filing at once; and why that beats a loop.
- **Resource estimation & scaling** — profiling a small run, estimating a bigger one, and checking your estimate against what the job actually used.
- **Reproducibility** — a README a colleague (or future you) can actually rerun.

And if you got into the bonus material: distilling today's conventions into a reusable
Claude skill, and what asking Slurm for a GPU does and doesn't buy you.

You now have the full loop every real research pipeline needs: **estimate → request → run → check → document.**

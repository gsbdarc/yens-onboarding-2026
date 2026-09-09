---
layout: default
title: "Part 1 Checkpoint"
parent: "Part 1 — Profile & Submit a Job"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 7
permalink: /day2/part1-checkpoint/
---

# Part 1 Checkpoint

You have measured what your script actually costs, and you have handed a job to the
scheduler instead of holding a terminal open. Part 2 takes that one job and turns it into
every filing at once — and it assumes all six of these work.

This checkpoint is how you find out. Six things, in one continuous run, about five
minutes. Do it **before you start Part 2**, while there is still someone circulating who
can fix whatever is broken.

{: .important }
> **A red sticky here is the cheapest one you will ever put up.** An array is the same
> script with one more flag — if your single job never ran, the array will fail the same
> way, times a hundred, and you will be debugging it during the block where the capstone
> lives.

---

## What You Should Be Able to Do

Six things. Each one you just worked through, and each has a check you can run.

| # | Skill | Where you learned it |
|---|---|---|
| 1 | Measure a script you have never seen — cores and RAM | [1. Profile the Mystery Script]({{ '/day2/profile-mystery-script/' | relative_url }}) |
| 2 | Time the batch script over 10 filings | [2. Profile the Batch Script]({{ '/day2/profile-batch-script/' | relative_url }}) |
| 3 | Write the three numbers down where the next step can read them | [3. Write Down What You Measured]({{ '/day2/resource-profile/' | relative_url }}) |
| 4 | Read the live queue, and tell `R` from `PD` | [4. Peek at the Queue]({{ '/day2/peek-at-the-queue/' | relative_url }}) |
| 5 | Write `#SBATCH` directives by hand and submit the job | [5. Submit]({{ '/day2/submit-a-slurm-job/' | relative_url }}) |
| 6 | Find out what the job did — including when it failed | [6. Read Logs]({{ '/day2/debug-a-failed-job/' | relative_url }}) |

The order matters, and it is the same order the morning ran in: you cannot write a
`#SBATCH` line until you have measured the number that goes in it, and you cannot tell
whether the job worked until you can read its logs. Items 1–3 produce the numbers;
items 4–6 spend them.

---

## The Run

{: .exercise }
> Work down the six. Run each check, and stop at the first one that doesn't do what it
> says — a later step failing is almost always an earlier step that only looked fine.

### 1 — You measured the mystery script

You should be able to say, from memory, whether `scripts/mystery_script.py` was serial or
parallel and roughly how much RAM it held. If you cannot, run it again — it only takes
thirty seconds, and this is the technique the whole day rests on.

```bash
cd ~/yens-onboarding-2026
source .venv/bin/activate
time python scripts/mystery_script.py
```

While it runs, in your **second** terminal on the **same** node:

```bash
htop -u $USER      # q to quit
```

A pass is being able to answer both questions out loud: how many workers, and how much
memory each. If `htop` showed you one process, you were on the wrong node — the second
terminal has to be on the same Yen as the first.

### 2 — You timed the batch script

```bash
time python scripts/extract_form_3_batch.py
```

You are looking at the three numbers `time` prints. `real` is what you will put in
`--time`. That `user` is much *smaller* than `real` is the finding: the script spends most
of its life waiting on the network, not computing.

### 3 — The numbers are written down

Not remembered — written, in the file the next step reads from.

```bash
grep -A 8 "Resource Profile" README.md
```

Six lines with actual numbers in them. If this prints nothing, that is the checkpoint
failing, not a formality: the `#SBATCH` directives in item 5 come from here, and a number
you did not write down is a number you will guess at.

### 4 — You can read the queue

```bash
squeue --me                 # your jobs, probably empty right now
squeue | head -20           # everyone's
```

Find a job in each state. `R` is running; `PD` is pending, waiting for a node with the
resources it asked for. If everything is `R`, the cluster is quiet — say so, and look at
the `NODELIST` column instead to see which nodes are busy.

### 5 — You wrote and submitted a job

```bash
ls slurm/*.slurm            # the one you wrote should be here
mkdir -p logs
sbatch --reservation=class_day2 slurm/extract_form_3_batch.slurm
squeue --me
```

You should get `Submitted batch job` and a number back, and see your job appear. If
`sbatch` complains about the output path, `logs/` does not exist — Slurm resolves
`--output` at submit time, which is why `mkdir -p logs` comes first.

### 6 — You read the output

```bash
ls logs/
cat logs/extract_*.out
sacct -j JOBID --format=JobID,JobName,State,Elapsed,MaxRSS
```

Replace `JOBID` with your number. `State` should say `COMPLETED` and `MaxRSS` is what the
job really held — compare it against what you wrote in item 3.

You should also have seen a job **fail** and read the `.err` to find out why. That was
`slurm/fix_me.slurm`, and it is the half of this skill that matters most:

```bash
cat logs/fix_me_*.err
```

If you never ran it, run it now. Reading a failed job's error log is the thing you will do
most often for the rest of your time on the cluster.

---

## Before You Move On

{: .note }
> 🟢 **Green sticky** = all six ran &nbsp;&nbsp; 🔴 **Red sticky** = one of them didn't
>
> Put the sticky up before you stand up for coffee, not after — an instructor can come to
> you while you are away from the keyboard anyway.

If you are green on all six, you can do the thing this cluster is for: measure a job, ask
for exactly what it needs, hand it over, and find out what happened. Part 2 is the same
loop at a hundred times the scale.

{: .aside }
> Nothing here is specific to this course. Measure, request, run, check is the loop for any
> scheduler on any cluster — the flags change, the order does not.

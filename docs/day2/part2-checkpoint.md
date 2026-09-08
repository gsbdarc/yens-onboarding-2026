---
layout: default
title: "Part 2 Checkpoint"
parent: "Part 2 — Scale & Ship"
grand_parent: "Day 2 — The Cluster"
nav_order: 3
permalink: /day2/part2-checkpoint/
---

# Part 2 Checkpoint

This is the last thing in the two days. Four items, and unlike the Part 1 checkpoint
nothing downstream depends on them — so this one is for you, not for the next section.

It is worth running anyway. Two of the four are the capstone, and the capstone is the only
place in the two days where you commit to a number before you find out whether it was
right.

{: .important }
> **If you are short on time, do items 3 and 4.** An array you got working is a skill you
> can look up again; an estimate you wrote down and then checked against reality is the
> thing that changes how you size jobs next month.

---

## What You Should Be Able to Do

| # | Skill | Where you learned it |
|---|---|---|
| 1 | Submit one script that fans out into many independent tasks | [3. Run a Job Array]({{ '/day2/job-arrays/' | relative_url }}) |
| 2 | Make a task safe to run twice | [3. Run a Job Array]({{ '/day2/job-arrays/' | relative_url }}) |
| 3 | Estimate a bigger run's cost — in writing, before submitting | [4. Capstone]({{ '/day2/capstone/' | relative_url }}) |
| 4 | Compare what you asked for against what the job used | [4. Capstone]({{ '/day2/capstone/' | relative_url }}) |

---

## The Run

{: .exercise }
> Four checks. The first two are quick; the last two are reading back what you already
> wrote.

### 1 — An array ran, and fanned out

```bash
ls logs/hello_*
```

You should see **four** pairs of files, not one — `logs/hello_<jobid>_1.out` through
`_4.out`. That is the whole point of an array: one submission, four independent tasks,
four separate logs.

```bash
cat logs/hello_*_*.out
```

Four lines, each naming a different task number. If you see one file with one line, you
submitted `slurm/hello.slurm` rather than `slurm/hello_array.slurm`.

### 2 — Your tasks are rerun-safe

Submit your 100-filing array a second time and watch what happens.

```bash
sbatch --reservation=class_day2 slurm/extract_array.slurm
squeue --me
```

It should finish in **seconds**, not minutes, because every task finds its output already
on disk and exits immediately. If it runs for the full time again, the existence check is
missing or is looking at the wrong path — and at 992 filings that is the difference
between a re-run costing nothing and costing the whole job again.

### 3 — The estimate is in writing

```bash
grep -A 10 "100 filings" README.md
```

You are looking for the numbers you wrote **before** you submitted: time, cores, RAM. If
they are not there, the capstone did not happen — write them now from what you remember
predicting, and be honest about it.

### 4 — And you checked it

```bash
sacct -j JOBID --format=JobID,State,Elapsed,MaxRSS,ReqTRES
```

Then look at your README and confirm the actuals sit next to the estimate, with a note on
which way you were wrong. Being wrong is the expected outcome — ten times the data is
rarely ten times the time and almost never ten times the memory. The number worth having
is the gap.

---

## Before You Go

{: .note }
> 🟢 **Green sticky** = all four ran &nbsp;&nbsp; 🔴 **Red sticky** = one of them didn't
>
> This is also the moment to ask the question you have been saving. The room empties fast
> and the answer is easier in person than over Slack.

You started yesterday with a script that ran one filing on a machine you share. You are
leaving with one that runs a thousand on hardware you asked for by name, and a written
record of what it cost.

**Where to go next:** [Where to Go Next]({{ '/day2/where-to-go-next/' | relative_url }})
has Slack, RCpedia and the email address. If you finished early, the bonus sections are
[GPUs]({{ '/day2/gpus/' | relative_url }}) and
[Writing a Slurm Job with Claude]({{ '/day2/slurm-with-claude/' | relative_url }}).

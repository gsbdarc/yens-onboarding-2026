---
layout: default
title: "Part 1 — Profile & Submit a Job"
parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 1
has_children: true
has_toc: false
permalink: /day2/part1/
---

# Part 1 — Profile & Submit a Job

Yesterday's script runs, on one filing at a time, on an interactive Yen node you share
with everyone else. This part is finding out what it actually costs — and then handing it
to the scheduler instead of holding a terminal open.

| Section | Give it about |
|---|---|
| [1. Profile]({{ '/day2/profiling/' | relative_url }}) | 22 min |
| [2. Document]({{ '/day2/resource-profile/' | relative_url }}) | 5 min |
| [3. Peek at the Queue]({{ '/day2/peek-at-the-queue/' | relative_url }}) | 5 min |
| [4. Submit]({{ '/day2/submit-a-slurm-job/' | relative_url }}) | 25 min |
| [5. Read Logs]({{ '/day2/debug-a-failed-job/' | relative_url }}) | 8 min |
| [Part 1 Checkpoint]({{ '/day2/part1-checkpoint/' | relative_url }}) | 5 min |

If you are well past one of these, put up a red sticky rather than pushing on — falling
behind quietly is the failure mode this hour is trying to avoid.

Each section is marked **Mandatory** or **Bonus**. Do the mandatory ones in order — they
build on each other, and the numbers you write down in one are the inputs to the next.

**Take your own breaks** inside the work block. There is no whole-room break today; stand
up and get coffee when your table reaches a natural stopping point.

{: .important }
> **If you finish the mandatory exercises early, check whether anyone at your table is
> stuck before you move on to the bonus material.** Explaining a thing you just learned is
> the fastest way to find out whether you actually learned it.

---

## Sections

| Section | Format | What you'll learn |
|---|---|---|
| [1. Profile]({{ '/day2/profiling/' | relative_url }}) | 💻 Mandatory | Measure a script you have never seen, then the real workload over 10 filings |
| [2. Document]({{ '/day2/resource-profile/' | relative_url }}) | 💻 Mandatory | Put the three numbers in your README, where the next step reads them |
| [3. Peek at the Queue]({{ '/day2/peek-at-the-queue/' | relative_url }}) | 💻 Mandatory | Read the live queue and tell `R` from `PD` |
| [4. Submit]({{ '/day2/submit-a-slurm-job/' | relative_url }}) | 💻 Mandatory | Write `#SBATCH` directives by hand, submit, monitor, cancel, read the logs |
| [5. Read Logs]({{ '/day2/debug-a-failed-job/' | relative_url }}) | 💻 Mandatory | Submit a job that fails on purpose, and find out why from its `.err` |
| [Part 1 Checkpoint]({{ '/day2/part1-checkpoint/' | relative_url }}) | ✅ Checkpoint | Six checks proving the things Part 2 depends on actually work |

{: .note }
> **Submit It to Slurm is the protected one.** If this part runs long, it is the section to
> protect — writing the directives by hand, hitting the `logs/` and fresh-shell gotchas,
> and reading a failed job's `.err` is the most useful half hour of the two days. The two
> bonuses after the checkpoint are genuinely optional.
>
> The [Part 1 Checkpoint]({{ '/day2/part1-checkpoint/' | relative_url }}) is the hinge:
> everything in Part 2 assumes its six items work, so run it before you move on while
> there is still someone circulating who can help.

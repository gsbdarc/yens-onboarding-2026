---
layout: default
title: "Part 1 — Measure & Submit"
parent: "Day 2 — The Cluster"
nav_order: 1
has_children: true
has_toc: false
permalink: /day2/part1/
---

# Part 1 — Measure & Submit

Yesterday's script runs, on one filing at a time, on a machine you share with everyone
else. This part is finding out what it actually costs — and then handing it to the
scheduler instead of holding a terminal open.

**Lecture 9:00–9:20, then the lab until 10:30.** Seventy minutes, self-paced, while we
circulate. The lecture covers what a core, RAM and the queue actually are; this part is
where you measure them and hand a job over.

| Section | Give it about |
|---|---|
| [1. Profile a Script]({{ '/day2/profiling/' | relative_url }}) | 25 min |
| [2. Submit It to Slurm]({{ '/day2/slurm-job/' | relative_url }}) | 40 min |
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
| [1. Profile a Script]({{ '/day2/profiling/' | relative_url }}) | 💻 Mandatory | Measure a script's time, cores and memory instead of guessing at them |
| [2. Submit It to Slurm]({{ '/day2/slurm-job/' | relative_url }}) | 💻 Mandatory | Read the queue, write `#SBATCH` directives by hand, submit, monitor, and debug a real job |
| [Part 1 Checkpoint]({{ '/day2/part1-checkpoint/' | relative_url }}) | ✅ Checkpoint | Six checks proving the things Part 2 depends on actually work |
| [Size Your Own Machine]({{ '/day2/compute-environments/' | relative_url }}) | ⭐ Bonus | Put your own laptop's cores and RAM against a Yen node, and price it in the cloud |
| [Writing a Slurm Job with Claude]({{ '/day2/slurm-with-claude/' | relative_url }}) | ⭐ Bonus | Distill the Yens conventions you just learned into a reusable Claude skill |

{: .note }
> **Submit It to Slurm is the protected one.** If this part runs long, it is the section to
> protect — writing the directives by hand, hitting the `logs/` and fresh-shell gotchas,
> and reading a failed job's `.err` is the most useful half hour of the two days. The two
> bonuses after the checkpoint are genuinely optional.
>
> The [Part 1 Checkpoint]({{ '/day2/part1-checkpoint/' | relative_url }}) is the hinge:
> everything in Part 2 assumes its six items work, so run it before you move on while
> there is still someone circulating who can help.

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

**9:00 to 10:30.** A short lecture on CPU, RAM and the queue, then a long work block where
you go at your own pace while we circulate.

Each section is marked **Mandatory** or **Bonus**. Do the mandatory ones in order — they
build on each other, and the numbers you write down in one are the inputs to the next.

**Take your own breaks** inside the work block. There is no whole-room break today; stand
up and get coffee when your table reaches a natural stopping point.

{: .important }
> **If you finish the mandatory exercises early, check whether anyone at your table is
> stuck before you move on to the bonus material.** Explaining a thing you just learned is
> the fastest way to find out whether you actually learned it.

---

## Before You Start

Three things need to be in place. **Say so now if any of them are missing:**

1. Your fork, cloned to the Yens at `~/yens-onboarding-2026`
2. A virtual environment at `~/yens-onboarding-2026/.venv`, with `requirements.txt` installed
3. A `.env` holding your `ANTHROPIC_API_KEY`, and `.env` in `.gitignore`

Today profiles `scripts/extract_form_3_batch.py`, which is committed in the repo — everyone
starts from the same working script. If your own version from Day 1 runs, profile that one
instead.

---

## Sections

| Section | Format | What you'll learn |
|---|---|---|
| [Compute Environments]({{ '/day2/compute-environments/' | relative_url }}) | 💬 Lecture + discussion | CPU, RAM, and storage — and how your laptop, the Yens, and the cloud trade off |
| [Profiling Resource Usage]({{ '/day2/profiling/' | relative_url }}) | 💻 Mandatory | Measure a script's time, CPU, and memory instead of guessing at them |
| [The Slurm Scheduler]({{ '/day2/slurm-scheduler/' | relative_url }}) | 💻 Mandatory | Why a shared cluster needs a scheduler; read the live queue and the partitions |
| [Writing & Submitting a Slurm Job]({{ '/day2/slurm-job/' | relative_url }}) | 💻 Mandatory | Write a batch script line by line; submit, monitor, cancel, and debug a real job |
| [Writing a Slurm Job with Claude]({{ '/day2/slurm-with-claude/' | relative_url }}) | ⭐ Bonus | Distill the Yens conventions you just learned into a reusable Claude skill |

{: .note }
> **Writing & Submitting a Slurm Job is the protected one.** If this part runs long,
> it is the section to protect — writing the directives by hand, hitting the `logs/` and
> fresh-shell gotchas, and reading a failed job's `.err` is the most useful half hour of
> the two days. The Claude bonus after it is genuinely optional.

---
layout: default
title: "Day 2 — The Cluster"
nav_order: 3
has_children: true
has_toc: false
permalink: /day2/
---

# Day 2 — The Cluster

Yesterday's script works, on one filing at a time, on a shared machine. Today you
find out what it actually costs to run, hand it to a scheduler, and scale it across
the cluster — then write the README that makes it rerunnable.

---

## How Today Works

Same shape as yesterday: a short lecture, then a long block where you work at your own
pace while we circulate.

| Clock | |
|---|---|
| 9:00–9:20 | Lecture — CPU, RAM, and the queue |
| 9:20–10:30 | **Work block 1** — profile it, then hand it to Slurm |
| 10:30–10:50 | Lecture — scaling out |
| 10:50–11:50 | **Work block 2** — job arrays, then the capstone |
| 11:50–12:00 | Wrap-up and questions |

Each section is marked **Mandatory** or **Bonus**. Do the mandatory ones in order — they
build on each other, and the numbers you write down in one are the inputs to the next.

**Take your own breaks** inside the work blocks. There is no whole-room break today;
stand up and get coffee when your table reaches a natural stopping point.

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
| [Writing a Slurm Job with Claude]({{ '/day2/slurm-with-claude/' | relative_url }}) | ⭐ Bonus | Distil the Yens conventions you just learned into a reusable Claude skill |
| [Slurm Job Arrays]({{ '/day2/job-arrays/' | relative_url }}) | 💻 Mandatory | One script, one `--array` flag, every filing processed at once |
| [Day 2 Capstone]({{ '/day2/capstone/' | relative_url }}) | 🔑 Mandatory | Estimate the resources for a bigger run, submit it, then check your estimate against `sacct` |
| [GPUs]({{ '/day2/gpus/' | relative_url }}) | ⭐ Bonus | Request a GPU, see what you landed on, and work out whether your job wanted one |
| [Where to Go Next]({{ '/day2/where-to-go-next/' | relative_url }}) | 📣 Wrap-up | Slack, RCpedia, and where to ask for help |

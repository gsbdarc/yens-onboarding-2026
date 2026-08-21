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

**9:00–12:00, with breaks at 10:00 and 11:00.**

---

## Day 1 Recap

Five things need to be in place. **Say so now if any of them are missing** — the
9:20 profiling section profiles the script from item 4, and everything after that
builds on it. We have a working copy we can hand you.

1. Your fork, cloned to the Yens at `~/yens-onboarding-2026`
2. A virtual environment at `~/yens-onboarding-2026/.venv`, with `requirements.txt` installed
3. A `.env` holding your Stanford AI API Gateway key, and `.env` in `.gitignore`
4. **A working `scripts/extract_form_3_batch.py` run** — results in `results/`, from the between-days assignment
5. Claude Code installed and signed in

---

## Sections

| Section | Format | What you'll learn |
|---|---|---|
| [Compute Environments]({{ '/day2/compute-environments/' | relative_url }}) | 💬 Demo + discussion | CPU, RAM, and storage — and how your laptop, the Yens, and the cloud trade off |
| [Profiling Resource Usage]({{ '/day2/profiling/' | relative_url }}) | 💻 Hands-on | Measure a script's time, CPU, and memory instead of guessing at them |
| [The Slurm Scheduler]({{ '/day2/slurm-scheduler/' | relative_url }}) | 💻 Hands-on | Why a shared cluster needs a scheduler; read the live queue and the partitions |
| [Writing & Submitting a Slurm Job]({{ '/day2/slurm-job/' | relative_url }}) | 💻 Hands-on | Write a batch script line by line; submit, monitor, cancel, and debug a real job |
| [Writing a Slurm Job with Claude]({{ '/day2/slurm-with-claude/' | relative_url }}) | 👀 Demo | Distil the Yens conventions you just learned into a reusable Claude skill |
| [Slurm Job Arrays]({{ '/day2/job-arrays/' | relative_url }}) | 💻 Hands-on | One script, one `--array` flag, every filing processed at once |
| [Day 2 Capstone]({{ '/day2/capstone/' | relative_url }}) | 🔑 Capstone | Estimate the resources for a bigger run, submit it, then check your estimate against `sacct` |
| [Where to Go Next]({{ '/day2/where-to-go-next/' | relative_url }}) | 📣 Wrap-up | GPUs and local LLMs, Slack, RCpedia, and where to ask for help |

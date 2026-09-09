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

---

## Sections

| Section | Format | What you'll learn |
|---|---|---|
| [1. Profile]({{ '/day2/profiling/' | relative_url }}) | 💻 Hands-on | Measure a script you have never seen, then the real workload over 10 filings |
| [2. Document]({{ '/day2/resource-profile/' | relative_url }}) | 💻 Hands-on | Put the three numbers in your README, where the next step reads them |
| [3. Submit]({{ '/day2/submit-a-slurm-job/' | relative_url }}) | 💻 Hands-on | Read the live queue, then write `#SBATCH` directives by hand, submit, monitor and cancel |
| [4. Read Logs]({{ '/day2/debug-a-failed-job/' | relative_url }}) | 💻 Hands-on | Submit a job that fails on purpose, and find out why from its `.err` |
| [Part 1 Checkpoint]({{ '/day2/part1-checkpoint/' | relative_url }}) | ✅ Checkpoint | Measure a script, write the numbers down, hand it to Slurm, and read what came back |

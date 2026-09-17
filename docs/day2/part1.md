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

**9:00 to 10:30.** A short lecture, then the work block.

{: .important }
> **First, get back on the Yens.** Pick one of the five Yens and open its JupyterHub, then log
> in with your SUNetID:
>
> [yen1](https://yen1.stanford.edu/jupyter/) ·
> [yen2](https://yen2.stanford.edu/jupyter/) ·
> [yen3](https://yen3.stanford.edu/jupyter/) ·
> [yen4](https://yen4.stanford.edu/jupyter/) ·
> [yen5](https://yen5.stanford.edu/jupyter/)
>
> Click the **blue "+"** to open the Launcher and open a **Terminal** — no `ssh`, and no Duo
> prompt. Blocks labelled **JupyterHub Terminal** and **Yen Terminal** both go at that shell
> prompt; a **Jupyter Notebook Cell** does not.

---

## Hands-On Lab

| | What you'll learn | Bonus |
|---|---|---|
| [1. Profile]({{ '/day2/profiling/' | relative_url }}) | Measure a script you have never seen, then the real workload over 10 filings | Profile two more scripts · explore real cluster usage data · size up your own machine |
| [2. Document]({{ '/day2/resource-profile/' | relative_url }}) | Put the three numbers in your README, where the next step reads them | Let Claude write it into the README |
| [3. Submit]({{ '/day2/submit-a-slurm-job/' | relative_url }}) | Read the live queue, then write `#SBATCH` directives by hand, submit, monitor and cancel | Other ways to run and inspect jobs · turn this into a Claude skill |
| [4. Read Logs]({{ '/day2/debug-a-failed-job/' | relative_url }}) | Submit a job that fails on purpose, and find out why from its `.err` | Three more broken jobs · let Claude read the log for you |

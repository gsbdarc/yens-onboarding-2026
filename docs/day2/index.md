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

**9:00–12:00.** Two short lectures, each followed by a self-paced hour in which everyone
reaches a checkpoint. Instructors circulate rather than lead, so put up a red sticky
whenever you want one.

| Clock | | |
|---|---|---|
| 9:00–9:20 | Lecture 1 | Where your code runs, and who decides |
| 9:20–10:30 | **Part 1 lab** | Profile it, then hand it to Slurm |
| 10:30–10:50 | Lecture 2 | Scaling out |
| 10:50–11:50 | **Part 2 lab** | Scale it, then size it |
| 11:50–12:00 | Wrap + Q&A | |

Each section is marked **Mandatory** or **Bonus**. Do the mandatory ones in order — they
build on each other, and the numbers you write down in one are the inputs to the next.

**Take your own breaks** inside the work blocks. There is no whole-room break today;
stand up and get coffee when your table reaches a natural stopping point.

---

## The Two Parts

| Part | Clock | What it is |
|---|---|---|
| [Part 1 — Measure & Submit]({{ '/day2/part1/' | relative_url }}) | 9:00–10:30 | What the script actually costs in CPU, RAM and time — then hand it to the scheduler. Ends in a checkpoint |
| [Part 2 — Scale & Ship]({{ '/day2/part2/' | relative_url }}) | 10:30–12:00 | One job becomes every filing at once; predict a bigger run's cost, then check the prediction. Ends in a checkpoint |

---

## Before You Start

Three things need to be in place. **Say so now if any of them are missing:**

1. Your fork, cloned to the Yens at `~/yens-onboarding-2026`
2. A virtual environment at `~/yens-onboarding-2026/.venv`, with `requirements.txt` installed
3. A `.env` holding your `ANTHROPIC_API_KEY`, and `.env` in `.gitignore`

Today profiles `scripts/extract_form_3_batch.py`, which is committed in the repo — everyone
starts from the same working script. If your own version from Day 1 runs, profile that one
instead.

{: .important }
> **If you finish the mandatory exercises early, check whether anyone at your table is
> stuck before you move on to the bonus material.** Explaining a thing you just learned is
> the fastest way to find out whether you actually learned it.

{: .note }
> **The [Part 1 Checkpoint]({{ '/day2/part1-checkpoint/' | relative_url }}) is the hinge.**
> Everything in Part 2 assumes its six items work, so run it before the second lecture
> while there is still someone circulating who can help with whatever is broken.

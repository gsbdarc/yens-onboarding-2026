---
layout: default
title: "Part 2 — Submit a Job Array"
parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 2
has_children: true
has_toc: false
permalink: /day2/part2/
---

# Part 2 — Submit a Job Array

One job at a time is not why you came to a cluster. This part turns the single job you
just submitted into every filing at once, then asks you to predict what a bigger run will
cost *before* you run it — and check your prediction against what actually happened.

This is the block that has historically run out of clock, so if you get ahead, spend the
time helping your table rather than racing into the bonuses.

{: .important }
> This part assumes the [Part 1 Checkpoint]({{ '/day2/part1-checkpoint/' | relative_url }})
> passed. If your single job never submitted successfully, sort that out before starting the
> arrays — an array is the same script with one more flag, and it will fail the same way,
> a hundred times over.

---

## Sections

| Section | Format | What you'll learn |
|---|---|---|
| [1. Watch an Array Fan Out]({{ '/day2/array-fan-out/' | relative_url }}) | 💻 Hands-on | One submission, four tasks, four logs — the shortest proof an array works |
| [2. Run 100 Filings Through an Array]({{ '/day2/array-100-filings/' | relative_url }}) | 💻 Hands-on | The real thing: one script, one `--array` flag, 100 filings |
| [3. Make Your Tasks Rerun-Safe]({{ '/day2/rerun-safe-tasks/' | relative_url }}) | 💻 Hands-on | Make a task skip work it has already done, so a resubmit costs nothing |
| [4. Scale]({{ '/day2/capstone/' | relative_url }}) | 💻 Hands-on | Estimate a bigger run's cost, submit it, then check yourself against `sacct` |
| [Part 2 Checkpoint]({{ '/day2/part2-checkpoint/' | relative_url }}) | ✅ Checkpoint | Fan a job array out, make it safe to rerun, and size a bigger run before submitting it |

{: .note }
> **Write the estimate before you submit.** Scale is the one place in the two days
> where being wrong is the point — a guess you wrote down and then checked against `sacct`
> teaches you more than a correct number you never committed to.

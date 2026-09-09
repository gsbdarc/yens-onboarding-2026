---
layout: default
title: "Part 2 — Scale & Ship"
parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 2
has_children: true
has_toc: false
permalink: /day2/part2/
---

# Part 2 — Scale & Ship

One job at a time is not why you came to a cluster. This part turns the single job you
just submitted into every filing at once, then asks you to predict what a bigger run will
cost *before* you run it — and check your prediction against what actually happened.

Same rules as Part 1: **Mandatory** sections in order, **Bonus** ones if you get ahead, and
take your own breaks inside the block.

| Section | Give it about |
|---|---|
| [1. Watch an Array Fan Out]({{ '/day2/array-fan-out/' | relative_url }}) | 5 min |
| [2. Run 100 Filings Through an Array]({{ '/day2/array-100-filings/' | relative_url }}) | 25 min |
| [3. Make Your Tasks Rerun-Safe]({{ '/day2/rerun-safe-tasks/' | relative_url }}) | 5 min |
| [4. Capstone]({{ '/day2/capstone/' | relative_url }}) | 20 min |
| [Part 2 Checkpoint]({{ '/day2/part2-checkpoint/' | relative_url }}) | 5 min |

That leaves slack on purpose. This is the block that has historically run out of clock, so
if you are ahead, spend it helping your table rather than racing into the bonuses.

{: .important }
> This part assumes the [Part 1 Checkpoint]({{ '/day2/part1-checkpoint/' | relative_url }})
> passed. If your single job never submitted successfully, sort that out before starting the
> arrays — an array is the same script with one more flag, and it will fail the same way,
> a hundred times over.

---

## Sections

| Section | Format | What you'll learn |
|---|---|---|
| [1. Watch an Array Fan Out]({{ '/day2/array-fan-out/' | relative_url }}) | 💻 Mandatory | One submission, four tasks, four logs — the shortest proof an array works |
| [2. Run 100 Filings Through an Array]({{ '/day2/array-100-filings/' | relative_url }}) | 💻 Mandatory | The real thing: one script, one `--array` flag, 100 filings |
| [3. Make Your Tasks Rerun-Safe]({{ '/day2/rerun-safe-tasks/' | relative_url }}) | 💻 Mandatory | Make a task skip work it has already done, so a resubmit costs nothing |
| [4. Capstone]({{ '/day2/capstone/' | relative_url }}) | 🔑 Mandatory | Estimate a bigger run's cost, submit it, then check yourself against `sacct` |
| [Part 2 Checkpoint]({{ '/day2/part2-checkpoint/' | relative_url }}) | ✅ Checkpoint | Four checks closing out the two days |
| [GPUs]({{ '/day2/gpus/' | relative_url }}) | ⭐ Bonus | Request a GPU, see what you landed on, and work out whether your job wanted one |
| [Where to Go Next]({{ '/day2/where-to-go-next/' | relative_url }}) | 📣 Wrap-up | Slack, RCpedia, and where to ask for help |

{: .note }
> **Write the estimate before you submit.** The capstone is the one place in the two days
> where being wrong is the point — a guess you wrote down and then checked against `sacct`
> teaches you more than a correct number you never committed to.

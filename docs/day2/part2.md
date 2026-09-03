---
layout: default
title: "Part 2 — Scale & Ship"
parent: "Day 2 — The Cluster"
nav_order: 2
has_children: true
has_toc: false
permalink: /day2/part2/
---

# Part 2 — Scale & Ship

One job at a time is not why you came to a cluster. This part turns the single job you
just submitted into every filing at once, then asks you to predict what a bigger run will
cost *before* you run it — and check your prediction against what actually happened.

**10:30 to noon.** A short lecture on scaling out, then the second work block, then
wrap-up and questions.

Same rules as Part 1: **Mandatory** sections in order, **Bonus** ones if you get ahead, and
take your own breaks inside the block.

{: .important }
> This part assumes you have a Slurm job that runs. If yours never submitted successfully
> in [Writing & Submitting a Slurm Job]({{ '/day2/slurm-job/' | relative_url }}), sort that
> out before starting the arrays — an array is the same script with one more flag, and it
> will fail the same way, times ten.

---

## Sections

| Section | Format | What you'll learn |
|---|---|---|
| [Slurm Job Arrays]({{ '/day2/job-arrays/' | relative_url }}) | 💻 Mandatory | One script, one `--array` flag, every filing processed at once |
| [Day 2 Capstone]({{ '/day2/capstone/' | relative_url }}) | 🔑 Mandatory | Estimate the resources for a bigger run, submit it, then check your estimate against `sacct` |
| [GPUs]({{ '/day2/gpus/' | relative_url }}) | ⭐ Bonus | Request a GPU, see what you landed on, and work out whether your job wanted one |
| [Where to Go Next]({{ '/day2/where-to-go-next/' | relative_url }}) | 📣 Wrap-up | Slack, RCpedia, and where to ask for help |

{: .note }
> **Write the estimate before you submit.** The capstone is the one place in the two days
> where being wrong is the point — a guess you wrote down and then checked against `sacct`
> teaches you more than a correct number you never committed to.

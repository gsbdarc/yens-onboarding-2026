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

**Lecture 10:30–10:50, then the lab until 11:50.** Sixty minutes, self-paced. Same rules as
Part 1: **Mandatory** sections in order, **Bonus** ones if you get ahead, and take your own
breaks inside the block.

| Section | Give it about |
|---|---|
| [3. Run a Job Array]({{ '/day2/job-arrays/' | relative_url }}) | 30 min |
| [4. Capstone]({{ '/day2/capstone/' | relative_url }}) | 25 min |
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
| [3. Run a Job Array]({{ '/day2/job-arrays/' | relative_url }}) | 💻 Mandatory | One script, one `--array` flag, every filing processed at once |
| [4. Capstone]({{ '/day2/capstone/' | relative_url }}) | 🔑 Mandatory | Estimate a bigger run's cost, submit it, then check the estimate against `sacct` |
| [Part 2 Checkpoint]({{ '/day2/part2-checkpoint/' | relative_url }}) | ✅ Checkpoint | Four checks closing out the two days |
| [GPUs]({{ '/day2/gpus/' | relative_url }}) | ⭐ Bonus | Request a GPU, see what you landed on, and work out whether your job wanted one |
| [Where to Go Next]({{ '/day2/where-to-go-next/' | relative_url }}) | 📣 Wrap-up | Slack, RCpedia, and where to ask for help |

{: .note }
> **Write the estimate before you submit.** The capstone is the one place in the two days
> where being wrong is the point — a guess you wrote down and then checked against `sacct`
> teaches you more than a correct number you never committed to.

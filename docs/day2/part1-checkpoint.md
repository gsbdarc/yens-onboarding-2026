---
layout: default
title: "Part 1 Checkpoint"
parent: "Part 1 — Profile & Submit a Job"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 5
permalink: /day2/part1-checkpoint/
---

# Part 1 Checkpoint

You have measured what your script actually costs, and you have handed a job to the
scheduler instead of holding a terminal open. Part 2 takes that one job and turns it into
every filing at once — and it assumes all six of these work.

This page is the gate, not another exercise — there is nothing here to run. Work down the
list and see whether you can tick every line.

{: .important }
> **A red sticky here is the cheapest one you will ever put up.** An array is the same
> script with one more flag — if your single job never ran, the array will fail the same
> way, times a hundred, and you will be debugging it during the block where the scaling
> work lives.

---

## Before Part 2, You Should Have

- [ ] Profiled the mystery script, with two terminals on one node
- [ ] Timed the batch script over 10 filings
- [ ] Written the three numbers into your README
- [ ] Read the live queue, and told `R` from `PD`
- [ ] Written `#SBATCH` directives by hand and submitted the job
- [ ] Read what the job did — a working job's `.out`, and a failed job's `.err`

They run in sidebar order: the first two are on **1. Profile**, the third on
**2. Document**, the next two on **3. Submit**, and the last on **4. Read Logs**. Anything
you cannot tick, that is where to go.

The order matters, and it is the order the morning ran in: you cannot write a `#SBATCH`
line until you have measured the number that goes in it, and you cannot tell whether the
job worked until you can read its logs. The first three produce the numbers; the last
three spend them.

---

## Before You Move On

{: .note }
> 🔴 **Red sticky** = one of the six didn't run.
>
> 🟢 **Green sticky** = all six ran. You are on to the bonus work, and free to help
> anyone at your table who is still going.
>
> Put the sticky up before you stand up for coffee, not after — an instructor can come to
> you while you are away from the keyboard anyway.

If you are green on all six, you can do the thing this cluster is for: measure a job, ask
for exactly what it needs, hand it over, and find out what happened. Part 2 is the same
loop at a hundred times the scale.

{: .aside }
> Nothing here is specific to this course. Measure, request, run, check is the loop for any
> scheduler on any cluster — the flags change, the order does not.

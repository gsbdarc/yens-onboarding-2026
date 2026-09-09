---
layout: default
title: "Part 2 Checkpoint"
parent: "Part 2 — Submit a Job Array"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 5
permalink: /day2/part2-checkpoint/
---

# Part 2 Checkpoint

This is the last thing in the two days. Four items, and unlike the Part 1 checkpoint
nothing downstream depends on them — so this one is for you, not for the next section.

It is worth running anyway. Two of the four come from Scale, which is the only
place in the two days where you commit to a number before you find out whether it was
right.

{: .important }
> **If you are short on time, do items 3 and 4.** An array you got working is a skill you
> can look up again; an estimate you wrote down and then checked against reality is the
> thing that changes how you size jobs next month.

---

## You Should Have

- [ ] An array running from `slurm/hello_array.slurm` — one submission, four separate logs
- [ ] Tasks made rerun-safe, so a resubmit finishes in seconds
- [ ] An estimate for the bigger run, written down **before** you submitted it
- [ ] That estimate held against what the job actually used

The first two are on **1. Watch an Array Fan Out** and **3. Make Your Tasks Rerun-Safe**;
the last two are both **4. Scale**.

---

## Before You Go

{: .note }
> 🔴 **Red sticky** = one of the four didn't run.
>
> 🟢 **Green sticky** = all four ran. You are on to the bonus work, and free to help
> anyone at your table who is still going.
>
> This is also the moment to ask the question you have been saving. The room empties fast
> and the answer is easier in person than over Slack.

You started yesterday with a script that ran one filing on a machine you share. You are
leaving with one that runs a thousand on hardware you asked for by name, and a written
record of what it cost.

**Where to ask, after today:**

| | | |
|---|---|---|
| 💬 | [**#gsb-yen-users**](https://circlerss.slack.com/archives/C01JXJ6U4E5) | Slurm, storage, software — paste your error output |
| ✉️ | [**gsb_darcresearch@stanford.edu**](mailto:gsb_darcresearch@stanford.edu) | Anything you would rather not post in a channel |
| 📖 | [**rcpedia.stanford.edu**](https://rcpedia.stanford.edu) | The written documentation, including current limits |

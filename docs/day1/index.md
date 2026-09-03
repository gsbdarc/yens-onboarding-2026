---
layout: default
title: "Day 1 — Foundations & AI"
nav_order: 2
has_children: true
has_toc: false
permalink: /day1/
---

# Day 1 — Foundations & AI

By lunchtime today you will have logged in to the Yens, put your work under version
control, built a reproducible Python environment, and written a script that sends a
real SEC filing to a language model and validates what comes back. Tomorrow scales
that same script across the cluster.

**9:00–12:00, with breaks at 10:00 and 11:00.**

Every section is written to be worked through yourself rather than followed along: the
commands, the checks, and what to do when something goes wrong are all on the page.
Instructors circulate rather than lead, so put up a red sticky whenever you want one.

---

## The Two Parts

| Part | Clock | What it is |
|---|---|---|
| [Part 1 — Setup]({{ '/day1/part1/' | relative_url }}) | 9:00–10:00 | A machine you can reach, an identity it recognises, and an assistant that can drive both. Ends in a checkpoint |
| [Part 2 — Python & AI]({{ '/day1/part2/' | relative_url }}) | 10:10–12:00 | A Python environment that travels, a key kept out of git, and a real extraction pipeline |

{: .important }
> Today assumes only the two accounts from **[Before You Arrive]({{ '/prework/' | relative_url }})**:
> a GitHub account and Claude through Stanford. Everything else — the terminal, the Yens
> login, the access token — you set up here, starting from nothing. If either account is
> missing, flag it early rather than falling behind.

{: .note }
> **The [Part 1 Checkpoint]({{ '/day1/part1-checkpoint/' | relative_url }}) is the hinge.**
> Everything in Part 2 assumes its six items work, so run it before the 10:00 break while
> there is still someone circulating who can help with whatever is broken.

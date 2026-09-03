---
layout: default
title: "Yens Onboarding 2026"
nav_order: 0
permalink: /
---

# Yens Onboarding 2026

A two-day, hands-on introduction to research computing and AI tools at Stanford GSB,
for incoming PhD students and faculty. Over two mornings you will build one real
pipeline end to end: get onto the Yens cluster, put your work under version control,
send documents through Stanford's AI API Gateway, and scale the whole thing across
the cluster with Slurm.

Everything you learn here is standard practice at every research university. It
travels with you.

---

## Before You Arrive

**Two accounts, and that's all.** Neither needs a terminal, and you do not need to log in
to the Yens before Day 1 — see [Before You Arrive]({{ '/prework/' | relative_url }}).

1. **A [GitHub account](https://github.com/signup).** Free; use an existing one if you
   have it.
2. **[Claude, through Stanford](https://uit.stanford.edu/service/claude).** Stanford
   provides Claude for Education free to most people. **Request it early** — approval is
   not instant.

{: .important }
> **Yens access.** Faculty, PhD students, post-docs, and research fellows have access
> by default; others need a SUNet ID and faculty sponsorship. See
> [Access the Yens](https://rcpedia.stanford.edu/_getting_started/how_access_yens/) on
> RCpedia. You don't need to *log in* before Day 1, but the account has to **exist** by
> then — and getting one can take days, so check now rather than on the morning.

{: .note }
> In class: put a **🟢 green sticky** on your laptop lid when you're done with a step,
> and a **🔴 red sticky** if you're stuck, so an instructor can come to you.

---

## The Two Days

<div class="day-layout">
  <div class="day-card">
    <h3><a href="{{ '/day1/' | relative_url }}">Day 1 — Foundations &amp; AI</a></h3>
    <p>9:00–12:00</p>
  </div>
  <div class="day-skills">SSH &middot; cluster file system &middot; Git &amp; GitHub &middot; Claude Code &middot; Python environments &middot; Stanford AI Gateway &middot; API keys &middot; Pydantic validation</div>

  <div class="day-card">
    <h3><a href="{{ '/day2/' | relative_url }}">Day 2 — The Cluster</a></h3>
    <p>9:00–12:00</p>
  </div>
  <div class="day-skills">Resource profiling &middot; Slurm &middot; job lifecycle &amp; logs &middot; debugging failed jobs &middot; Claude skills &middot; job arrays &middot; resource estimation</div>
</div>

Both mornings run 9:00–12:00. Day 1 breaks at 10:00 and 11:00; Day 2 runs as two
self-paced blocks, where you break when your table reaches a stopping point. The
[Reference]({{ '/reference/' | relative_url }}) section holds the material we could not
fit — local LLMs, LLM-as-a-judge, `scp`, and more.

---

## The Running Project

Both days build one pipeline over the same dataset: **SEC Form 3 filings**, the public
disclosures insiders file when they acquire a position in a company. They are
unstructured text, and the job is to turn them into structured records you can
analyze.

| | What you build |
|---|---|
| **Day 1** | A script that reads one filing, extracts fields with an LLM, and validates them. Then ten filings. |
| **Day 2** | The same work, profiled, submitted to Slurm, and scaled with a job array. Plus the README that makes it rerunnable. |

Your `README.md` is the deliverable that grows across both days. It is also the thing
your future self will thank you for.

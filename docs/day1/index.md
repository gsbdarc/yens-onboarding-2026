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

{: .important }
> Today assumes only the two accounts from **[Before You Arrive]({{ '/prework/' | relative_url }})**:
> a GitHub account and Claude through Stanford. Everything else — the terminal, the Yens
> login, the access token — we do together, starting now. If either account is missing,
> flag it in the first ten minutes
> rather than falling behind.

---

## Sections

Work through them in order — each builds on the one before.

| Section | Format | What you'll learn |
|---|---|---|
| [Connecting to the Yens]({{ '/day1/connect-to-the-yens/' | relative_url }}) | 💻 Hands-on | Log in over SSH, and find your way around cluster storage, quotas, and software modules |
| [Git & GitHub for Research]({{ '/day1/git-and-github/' | relative_url }}) | 💻 Hands-on | Fork, clone, branch, commit, push — and why a research project wants version control |
| [Working with Claude Code]({{ '/day1/claude-code/' | relative_url }}) | 📖 Pre-read + 💻 hands-on | Concepts are pre-work; in class you set it up, learn the controls, and give it a real task |
| [Running Python on the Yens]({{ '/day1/python-on-the-yens/' | relative_url }}) | 💻 Hands-on | How `$PATH` decides which `python3` answers, and the three ways to run Python |
| [Python Environments]({{ '/day1/python-environments/' | relative_url }}) | 💻 Hands-on | Build an isolated venv and rebuild a whole project from its `requirements.txt` |
| [Stanford's AI Services]({{ '/day1/stanford-ai-services/' | relative_url }}) | 🖊️ Concept + demo | The AI Playground vs. the API Gateway, and which data-risk levels each is cleared for |
| [AI Agents & Data Privacy]({{ '/day1/ai-agents-and-data-privacy/' | relative_url }}) | 💬 Discussion | What agents send where, how to classify your data, and how to keep a pipeline defensible |
| [Managing API Keys]({{ '/day1/api-keys/' | relative_url }}) | 💻 Hands-on | Load a key from `.env`, keep it out of git, and know why a committed key is a leaked key |
| [Extracting Data with an LLM]({{ '/day1/extracting-data-with-an-llm/' | relative_url }}) | 💻 Hands-on | Your first API call, then structured fields out of a real SEC filing — validated with Pydantic |
| [Day 1 Capstone]({{ '/day1/capstone/' | relative_url }}) | 🔑 Capstone | Scale to 10 filings, document it, commit. **Keep going on your own afterwards** |

{: .note }
> The last two run as **one continuous block**: the guided build flows straight into
> scaling it. You are not expected to finish the capstone in the room — carry on with it in
> your own time. Day 2 does not depend on it: it profiles the copy of the batch script
> that ships in the repo, so everyone starts Day 2 from the same working code.

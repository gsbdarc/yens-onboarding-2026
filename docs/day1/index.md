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

**Part 1 is the first five sections, and you have until the 10:00 break — about an hour —
to get through the checkpoint at the end of it.**

You work through it yourself rather than following along: every command, check, and
what-to-do-when-it-breaks is on the page, and instructors circulate rather than lead. Put
up a red sticky whenever you want one. Self-directed, but not open-ended — keep an eye on
the clock:

| Section | Give it about |
|---|---|
| [Connecting to the Yens]({{ '/day1/connect-to-the-yens/' | relative_url }}) | 10 min |
| [Your Data on the Yens]({{ '/day1/your-data/' | relative_url }}) | 5 min |
| [Git & GitHub for Research]({{ '/day1/git-and-github/' | relative_url }}) | 13 min |
| [Working with Claude Code]({{ '/day1/claude-code/' | relative_url }}) | 20 min |
| [Part 1 Checkpoint]({{ '/day1/part1-checkpoint/' | relative_url }}) | 10 min |

If you are well past one of these, put up a red sticky rather than pushing on — falling
behind quietly is the failure mode this hour is trying to avoid. If you are ahead, the
**Optional Practice** at the end of most sections is there for you.

{: .important }
> Today assumes only the two accounts from **[Before You Arrive]({{ '/prework/' | relative_url }})**:
> a GitHub account and Claude through Stanford. Everything else — the terminal, the Yens
> login, the access token — you set up here, starting from nothing. If either account is
> missing, flag it early rather than falling behind.

---

## Sections

Work through them in order — each builds on the one before.

| Section | Format | What you'll learn |
|---|---|---|
| [Connecting to the Yens]({{ '/day1/connect-to-the-yens/' | relative_url }}) | 💻 Hands-on | Log in over SSH, and understand what a remote server is and why research uses one |
| [Your Data on the Yens]({{ '/day1/your-data/' | relative_url }}) | 💻 Hands-on | Home, projects and scratch — which are backed up, how to check your quota, and what's eating it |
| [Git & GitHub for Research]({{ '/day1/git-and-github/' | relative_url }}) | 💻 Hands-on | Fork, clone, branch, commit, push — and why a research project wants version control |
| [Working with Claude Code]({{ '/day1/claude-code/' | relative_url }}) | 📖 Read + 💻 hands-on | Concepts first, then you set it up, learn the controls, and give it a real task |
| [Part 1 Checkpoint]({{ '/day1/part1-checkpoint/' | relative_url }}) | ✅ Checkpoint | Ten minutes proving the six things Part 2 depends on actually work |
| [Running Python on the Yens]({{ '/day1/python-on-the-yens/' | relative_url }}) | 💻 Hands-on | How `$PATH` decides which `python3` answers, and the three ways to run Python |
| [Python Environments]({{ '/day1/python-environments/' | relative_url }}) | 💻 Hands-on | Build an isolated venv and rebuild a whole project from its `requirements.txt` |
| [Stanford's AI Services]({{ '/day1/stanford-ai-services/' | relative_url }}) | 🖊️ Concept + demo | The AI Playground vs. the API Gateway, and which data-risk levels each is cleared for |
| [AI Agents & Data Privacy]({{ '/day1/ai-agents-and-data-privacy/' | relative_url }}) | 💬 Discussion | What agents send where, how to classify your data, and how to keep a pipeline defensible |
| [Managing API Keys]({{ '/day1/api-keys/' | relative_url }}) | 💻 Hands-on | Load a key from `.env`, keep it out of git, and know why a committed key is a leaked key |
| [Extracting Data with an LLM]({{ '/day1/extracting-data-with-an-llm/' | relative_url }}) | 💻 Hands-on | Your first API call, then structured fields out of a real SEC filing — validated with Pydantic |
| [Day 1 Capstone]({{ '/day1/capstone/' | relative_url }}) | 🔑 Capstone | Scale to 10 filings, document it, commit. **Keep going on your own afterwards** |

{: .note }
> **The first five are Part 1.** The checkpoint closes it, and everything in Part 2
> assumes all six of its items work — so run it before you move on, while there is still
> someone circulating who can help with whatever is broken.

{: .note }
> The last two run as **one continuous block**: the guided build flows straight into
> scaling it. You are not expected to finish the capstone in the room — carry on with it in
> your own time. Day 2 does not depend on it: it profiles the copy of the batch script
> that ships in the repo, so everyone starts Day 2 from the same working code.

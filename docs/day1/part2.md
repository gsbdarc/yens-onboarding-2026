---
layout: default
title: "Part 2 — Python & AI"
parent: "Day 1 — Foundations & AI"
nav_order: 2
has_children: true
has_toc: false
permalink: /day1/part2/
---

# Part 2 — Python & AI

Part 1 got you a working setup. This part is what you do with it: a Python environment
that travels, a key kept out of git, and a script that sends a real SEC filing to a
language model and validates what comes back.

**10:10 to noon, with a break at 11:00.** Longer than Part 1 and less uniform — the
extraction arc at the end is the part that matters most, and it continues in your own time
after today.

{: .important }
> This part assumes the [Part 1 Checkpoint]({{ '/day1/part1-checkpoint/' | relative_url }})
> passed. If any of its six items is still broken, fix that first — a venv you cannot
> create or a fork you cannot push to will stop you here rather than politely waiting.

---

## Sections

Work through them in order — each builds on the one before.

| Section | Format | What you'll learn |
|---|---|---|
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

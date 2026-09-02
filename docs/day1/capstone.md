---
layout: default
title: "Day 1 Capstone"
parent: "Part 2 — Python & AI"
grand_parent: "Day 1 — Foundations & AI"
nav_order: 7
permalink: /day1/capstone/
---

# Day 1 Capstone

One filing proves the code runs. Ten filings prove it's a pipeline — and surface the
things a single happy-path run never does.

Everything you need you already built this morning — this runs straight on from the
extraction section, as one continuous block.

{: .important }
> **You are not expected to finish this in the room.** Carry on with it in your own time —
> nothing to submit. Day 2 profiles a batch script just like this one, and a working copy
> ships in the repo, so you will not be stuck tomorrow if you don't get to the end today.

---

## The Task

{: .exercise }
> Run your extraction across **10 filings**, write the results to `results/`,
> document the pipeline in your `README.md`, and commit and push the lot to your fork.

You are not writing anything new. `scripts/extract_form_3_batch.py` in your repo
already does the loop — it reads URLs from `data/aws_links.csv`, sends each filing
through the Gateway, validates the reply against your Pydantic model, and writes one
JSON file per filing into `results/`.

```bash
cd ~/yens-onboarding-2026
source .venv/bin/activate
python3 scripts/extract_form_3_batch.py
```

Then look at what came back:

```bash
ls results/ | wc -l          # how many filings produced a result?
cat results/*.json | head -40
```

{: .important }
> **Ten is deliberate.** Every filing is a paid API call, and `NUM_FILINGS` at the
> top of the script is set to 10 for exactly that reason. Resist the urge to raise
> it — tomorrow you'll estimate the cost of a bigger run *before* submitting it,
> which is the habit worth having.

---

## What to Look For

A loop that finishes is not a loop that worked. Before you commit, answer these:

1. **Did every filing produce a file?** If `ls results/ | wc -l` is fewer than 10,
   which ones are missing, and does the log say why?
2. **Did any field come back empty or obviously wrong?** Pydantic catches the wrong
   *type*; it cannot catch a plausible-looking wrong *answer*. Open two or three
   results and read them against the filing they came from.
3. **Would a second run give you the same answers?** You have no way to know yet.
   Note the question — it is the whole subject of
   [Handling LLM Failure Modes]({{ '/reference/llm-failure-modes/' | relative_url }}).

{: .note }
> Finding one bad extraction in ten is a **success**, not a setback. It tells you the
> error rate is non-zero at a scale where you can still read every record by hand —
> which is the only point at which that is affordable.

---

## Document It

Open `README.md` at your repo root and write the section a colleague would need to
rerun this without you. Four things, briefly:

- **What it does** — one sentence on the input and the output
- **How to run it** — the three commands above, exactly
- **Where the output lands** — `results/`, one JSON per filing, named how
- **What you noticed** — anything from *What to Look For*, including failures

Claude Code is good at the first three and useless at the fourth. Write that one
yourself.

{: .tip }
> Have Claude read it back as a first-time reader:
>
> ```
> > Read my README as someone who has never seen this project. What would stop you
> > from reproducing this run? Don't fix anything, just tell me what's missing.
> ```

---

## Commit and Push

Use Claude Code, with the skill you installed this morning:

```
> Use the github-for-research skill. Commit my results and README changes on a new
> branch with a message describing the 10-filing extraction run, then push and open
> a pull request.
```

Or by hand:

```bash
git add results/ README.md
git commit -m "Extract structured fields from 10 SEC Form 3 filings"
git push
```

**Zoom out:** what you just saved is a documented, version-controlled pipeline that
turns unstructured filings into validated records. Tomorrow it stops depending on
your terminal staying open.

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help

---

## Finished Early?

- The optional practice in [Extracting Data with an LLM]({{ '/day1/extracting-data-with-an-llm/' | relative_url }}) — listing available models, pricing a call, comparing a reasoning model against a plain one
- The leaked-key exercise in [Managing API Keys]({{ '/day1/api-keys/' | relative_url }})
- [LLM-as-a-Judge]({{ '/reference/llm-as-a-judge/' | relative_url }}), the extension assignment — a second model checks the first one's calls, and your code routes the contested ones to a human

---

## Day 1 — What You Learned

- **The cluster** — logging in over SSH, where files live, quotas, and `module load`
- **Version control** — fork, clone, branch, commit, push, and why research wants it
- **Claude Code** — models, permission modes, tokens, context, skills, and what data may never be sent
- **Python that travels** — `$PATH`, virtual environments, and rebuilding a project from `requirements.txt`
- **Stanford's AI services** — the Playground vs. the API Gateway, and the data-risk levels each is cleared for
- **Secrets** — a key in `.env`, out of git, and why a committed key is a leaked key
- **Structured extraction** — an API call, a Pydantic schema, validation that fails loudly, and a logged script
- **Judgment** — what leaves your machine, what it costs, and which calls stay human

Tomorrow: what this run actually costs in CPU, memory, and time — and how to hand it
to a scheduler so it runs without you.

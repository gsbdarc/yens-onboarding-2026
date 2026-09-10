---
layout: default
title: "Stanford's AI Services"
parent: "Part 2 — Python & AI"
grand_parent: "Day 1 — Foundations & AI"
nav_order: 3
permalink: /day1/stanford-ai-services/
---

# Stanford's AI Services

"Can I analyze this data with AI?" is really three questions: what risk level is the
data, what does its Data Use Agreement allow, and what is the service or machine cleared
to handle? The strictest answer wins.

This course uses two different routes on purpose. You will try Stanford's AI Playground
as a governed browser tool, then call Claude directly through Anthropic's API for the
public SEC-filings pipeline. The direct API gives this class more usable throughput and
native Anthropic features, but it does **not** inherit Stanford's approval for sensitive
data.

---

## Exercise

{: .important }
> **In this section:** Try Stanford's AI Playground, distinguish a browser playground
> from a programmatic API, classify the data before choosing a service, and understand
> why this course's public-data pipeline uses Anthropic directly.

## Three Independent Checks

### 1. Stanford's data-risk classification

![Stanford Data Risk]({{ "/assets/images/Stanford_data_risk.png" | relative_url }})

Read Stanford's current
<a href="https://uit.stanford.edu/guide/riskclassifications" target="_blank" rel="noopener noreferrer">data-risk classification guidance</a>.

### 2. The dataset's rules

A Data Use Agreement (DUA), license, IRB protocol, or contract can impose stricter rules
than a service technically supports. "De-identified" does not automatically mean "safe
to send to AI," and a vendor license may forbid automated analysis entirely.

### 3. The system and service

The Yens, a Stanford-managed AI service, and a vendor API are separate systems with
different approvals. A file can be allowed on one and forbidden on another. Nothing in
Python stops you from making the wrong transfer; responsibility sits with the researcher.

| Route used in this course | Purpose here | Course data rule |
|---|---|---|
| Stanford AI Playground | Manual browser demonstration | Follow Stanford's current approval and the dataset's rules |
| Stanford AI API Gateway | Institutional programmatic option, discussed for context | Use its current approval process, DRA/DUA, and project requirements |
| Direct Anthropic API | The SEC extraction exercises | **Public, Low Risk filings only** |

Stanford's current service directory and approval details are the authority—not this
course page. Check
<a href="https://uit.stanford.edu/ai/services" target="_blank" rel="noopener noreferrer">AI services at Stanford</a>
and the
<a href="https://uit.stanford.edu/service/ai-api-gateway/faqs" target="_blank" rel="noopener noreferrer">AI API Gateway FAQ</a>
before using research data.

{: .warning }
> Direct access to Anthropic is **not the same service** as Claude provisioned by Stanford
> and is not a shortcut around a DUA, IRB, Data Risk Assessment, or platform restriction.
> In this course it is limited to public SEC filings. For Moderate or High Risk data,
> stop and use the Stanford-approved route for that project.

### Classify These Five

For each item, decide whether it is Low, Moderate, or High Risk, then ask whether a DUA
could make the handling requirements stricter.

1. A published journal article
2. Social Security numbers
3. An unreleased internal financial projection
4. Student grades and transcripts
5. De-identified, aggregated survey results

<details markdown="1">
<summary>Answer key — click to reveal</summary>

| # | Item | Starting classification | Why |
|---|---|---|---|
| 1 | Published article | Low | Already public |
| 2 | Social Security numbers | High | Regulated personal identifiers |
| 3 | Internal projection | Moderate | Confidential business information |
| 4 | Grades and transcripts | Moderate | FERPA-protected education records |
| 5 | De-identified aggregate results | Often Low | Re-identification and contract terms still matter |

The classification is only the first check. A DUA, IRB protocol, or other agreement can
require stricter treatment.
</details>

---

## Stanford's Browser and API Routes

### AI Playground: a browser tool

The
<a href="https://uit.stanford.edu/aiplayground" target="_blank" rel="noopener noreferrer">Stanford AI Playground</a>
is a chat interface. A person types one prompt and reads one answer. Try it with a public,
Low Risk question such as:

> Explain the difference between a Python interpreter and a Jupyter kernel in two
> sentences.

This is useful for exploration, but clicking through thousands of filings is not a
research pipeline.

### AI API Gateway: Stanford's programmatic route

The
<a href="https://uit.stanford.edu/service/ai-api-gateway" target="_blank" rel="noopener noreferrer">Stanford AI API Gateway</a>
lets code call models under Stanford's service controls. It remains the institutional
route to evaluate when a research project needs Stanford governance, sensitive-data
approval, centralized budget controls, or access to several providers through one API.

**Playground and Gateway are not synonyms.** The Playground is the manual browser
interface; the Gateway is the API that the previous version of this course called from
Python.

---

## Why This Course Calls Anthropic Directly

In earlier classroom runs, many students sent requests at the same time through a shared
Stanford Gateway key. That synchronized load ran into rate limits and stalled the exercise.
For this public-data pipeline, the course now uses a directly provisioned Anthropic
organization with more usable headroom for the expected class traffic.

That is an operational choice for this workload, not a claim that Anthropic is unlimited
or universally faster. Anthropic applies organization- and workspace-level limits for
requests and input/output tokens. A request that exceeds them receives HTTP `429`, and
clients should respect `retry-after`. See Anthropic's
<a href="https://platform.claude.com/docs/en/api/rate-limits" target="_blank" rel="noopener noreferrer">rate-limit documentation</a>.

There is also a scaling feature difference. Stanford's
<a href="https://uit.stanford.edu/service/ai-api-gateway/faqs" target="_blank" rel="noopener noreferrer">Gateway FAQ</a>
currently says batch processing is unavailable and calls are handled individually.
Anthropic offers a native
<a href="https://platform.claude.com/docs/en/build-with-claude/batch-processing" target="_blank" rel="noopener noreferrer">Message Batches API</a>
with separate capacity for asynchronous work. We do **not** use that API in the core
exercise: synchronous calls make timing, logs, failures, and Day 2's Slurm scaling easier
to see. It is the next option to evaluate for a production-scale pipeline.

| Question | Stanford Playground / Gateway | Direct Anthropic in this course |
|---|---|---|
| Interface | Playground is manual; Gateway is programmatic | Native programmatic API |
| Classroom throughput | Previous shared-key run hit limits | Course org is provisioned for expected class load |
| Limit visibility | Depends on the Stanford allocation | Published RPM, input-token, and output-token limit model |
| Native async batch | Gateway FAQ says not currently available | Message Batches API available |
| Governance | Stanford-managed controls and approvals | Vendor commercial API terms; no Stanford-sensitive-data approval implied |
| Provider scope | Multiple models/providers may be available | Claude models only |

{: .note }
> We do not publish a numerical "Anthropic vs. Stanford" speed claim because Stanford
> does not publish a directly comparable classroom Gateway limit. The evidence is the
> prior class's observed throttling plus the headroom provisioned for this cohort.

---

## What Happens in the Course Pipeline

```text
public SEC filing on the Yens
        |
        | HTTPS request authenticated by ANTHROPIC_API_KEY
        v
Anthropic Messages API
        |
        | text or schema-constrained response
        v
your Python process validates and saves the result
```

The prompt and filing leave the Yens. Anthropic states that commercial API inputs and
outputs are not used to train generative models unless the customer opts in, and its
standard retention is 30 days subject to documented exceptions. Read the current
<a href="https://privacy.anthropic.com/en/articles/7996885-how-do-you-use-personal-data-in-model-training" target="_blank" rel="noopener noreferrer">commercial training policy</a>
and
<a href="https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data" target="_blank" rel="noopener noreferrer">retention policy</a>
instead of assuming that "direct" means "local" or "not stored."

Next, [AI Agents & Data Privacy]({{ '/day1/ai-agents-and-data-privacy/' | relative_url }})
turns that flow into a repeatable decision. Then [Managing API Keys]({{ '/day1/api-keys/' | relative_url }})
sets up the direct Anthropic credential without putting it in Git.

---

## Skills Learned

- A playground is a person-facing chat interface; an API is a program-facing interface
- Stanford's Gateway and Anthropic's direct API are different routes with different governance
- Data classification, dataset terms, and system approval are independent checks
- Direct Anthropic is used here for expected classroom throughput and native features, only on public data
- Rate limits still exist; `429` and `retry-after` are normal operational signals

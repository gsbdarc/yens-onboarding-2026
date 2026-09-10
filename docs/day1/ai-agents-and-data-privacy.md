---
layout: default
title: "AI Agents & Data Privacy"
parent: "Part 2 — Python & AI"
grand_parent: "Day 1 — Foundations & AI"
nav_order: 4
permalink: /day1/ai-agents-and-data-privacy/
---

# AI Agents & Data Privacy

An API call sends exactly what your code puts in the request. An AI coding agent can
gather files, terminal output, and conversation history for you. Either way, model input
leaves the Yens when the model is remote. This section makes that movement explicit so
you can choose an approved route and build a pipeline someone else can audit.

---

## Exercise

{: .important }
> **In this section:** Identify what an API or coding agent sends, match the data to an
> approved service, understand token usage and rate limits, and design a defensible
> research pipeline.

This is a discussion block. No code.

## Models, Tokens, and Context

A language model reads **tokens**: chunks of text that are often smaller than a word.
The **context window** is everything available for the current response—your instructions,
data, schema, earlier messages, and any material a tool gathered. The model combines that
context with what it learned during training.

Two consequences matter for research:

- If text is in the context, it was sent to the model service.
- Input and output tokens determine API usage, cost, and whether you hit a rate limit.

The extraction script makes this easy to see: your system prompt and the SEC filing are
input; Claude's answer is output. Later you will inspect `response.usage.input_tokens` and
`response.usage.output_tokens` rather than guessing from word counts.

## API Calls and Coding Agents

An API call is comparatively explicit:

```text
the strings your code supplies -> remote model -> returned response
```

A coding agent is a **harness** around a model. It may read files, run commands, inspect
errors, and use tools. To ask the remote model what to do next, it assembles some of those
materials into context. Depending on the tool and task, that can include:

- the file being edited and nearby files
- conversation history and instructions
- terminal output, stack traces, and command results
- data samples pasted into source code or logs

An agent does not reliably classify sensitive material for you. Limit what it can read,
review its proposed actions, and treat everything in its context as data sent to its model
service.

## How Researchers Use These Systems

1. **Extract information from unstructured text.** A model applies a coding scheme to
   filings, transcripts, contracts, or survey responses. Today's Form 3 pipeline is this
   pattern at a small, inspectable scale.
2. **Build the pipeline.** A coding agent helps write loops, logs, validation, and Slurm
   jobs. The researcher remains responsible for design, review, and data handling.
3. **Study AI itself.** If people interact with AI as research participants, consent,
   human-subjects review, and participant data return to the center of the design.

{: .note }
> **Discuss:** Which pattern is closest to your work? What would a wrong answer cost—a
> noisy estimate, disclosure of protected data, or a decision affecting a person? The
> answer determines how much review and validation are enough.

## Choose the Route from the Data

Start with three independent checks from
[Stanford's AI Services]({{ '/day1/stanford-ai-services/' | relative_url }}):

1. Stanford's classification of the data
2. the DUA, license, IRB protocol, or contract
3. the approval of both the computing system and the model service

| Data or task | Course guidance |
|---|---|
| Public SEC filing | Direct Anthropic API is in scope for these exercises |
| Moderate or High Risk research data | Do not use the course's direct key; consult the project's Stanford-approved route |
| PHI or regulated identifiers | Stop and complete the required Stanford review and platform selection |
| DUA forbids AI or external processing | Do not send it, even if a tool is technically capable |

The
<a href="https://uit.stanford.edu/ai/services" target="_blank" rel="noopener noreferrer">Stanford AI services directory</a>
and your project's approval are the current authorities. Direct Anthropic, Stanford's
Claude offering, the AI Playground, and the AI API Gateway are different services; an
approval for one does not automatically transfer to another.

{: .warning }
> "The model is Claude" is not enough information to make a privacy decision. You must
> know **which account, contract, API route, and data-processing terms** are in use.

### Direct Anthropic in This Course

This course sends public, Low Risk SEC filings to Anthropic's commercial API. Anthropic's
published commercial terms say API inputs and outputs are not used to train generative
models unless the customer opts in. Standard retention is 30 days, with documented
exceptions. Check the current
<a href="https://privacy.anthropic.com/en/articles/7996885-how-do-you-use-personal-data-in-model-training" target="_blank" rel="noopener noreferrer">training policy</a>
and
<a href="https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data" target="_blank" rel="noopener noreferrer">retention policy</a>
for real projects.

These terms explain what the vendor does; they do not override Stanford policy or a DUA.

## Keep Sensitive Material Out of Context

- Put credentials in `.env`, keep `.env` ignored by Git, and never paste its contents
  into a prompt, notebook output, screenshot, or log.
- Do not include real records in comments, fixtures, stack traces, or example prompts.
- Give an agent the smallest workspace and file set it needs.
- Exclude restricted data and generated results from indexing when the tool supports it.
- Use synthetic or public examples while developing the code.
- Review a tool's account and data terms before assuming Stanford's agreement applies.

{: .note }
> **Discuss:** A Slurm script contains only a path to a restricted file. Does the model
> see the underlying file? What changes if a stack trace prints one row of that file, or a
> comment includes a real participant name?

## Cost and Throughput Are Different Limits

API work is constrained by both money and traffic. Anthropic reports usage on every
response:

```python
print(response.usage.input_tokens)
print(response.usage.output_tokens)
```

Use those values with the current model price when estimating a run. Separately,
Anthropic limits requests per minute and input/output tokens per minute at the
organization or workspace level. Exceeding a limit returns HTTP `429`; the response's
`retry-after` value tells a client when to try again. See the current
<a href="https://platform.claude.com/docs/en/api/rate-limits" target="_blank" rel="noopener noreferrer">rate-limit documentation</a>.

Why the distinction matters:

| Limit | Question to ask | Failure signal |
|---|---|---|
| Cost | Can the project afford all records at this model's price? | Unexpected spend |
| Request rate | Are too many calls starting together? | HTTP `429` |
| Input-token rate | Are documents too large or too concurrent? | HTTP `429` |
| Output-token rate | Are responses too long or too concurrent? | HTTP `429` |

The previous course's shared Stanford Gateway key was throttled when a roomful of students
called it together. The direct Anthropic organization for this course is provisioned with
more expected headroom, but it still has limits. The beginner scripts intentionally do
not hide `429` errors behind automatic retries: seeing the failure is part of learning
what happened. A production pipeline should add bounded retries that respect
`retry-after`, log each retry, and avoid duplicating successful work.

## Build a Defensible Pipeline

Before scaling beyond a sample:

1. **Classify the data and record the approved route.** Include DUA/IRB constraints.
2. **Measure a representative sample.** Record latency and input/output tokens; calculate
   expected cost without inventing a throughput guarantee.
3. **Validate the shape.** Use a schema so missing or mistyped fields fail loudly.
4. **Validate the meaning.** Manually compare a sample of results with source filings.
5. **Log decisions and failures.** Record model id, prompt version, failed records, and
   retry behavior without logging secrets or protected content.
6. **Keep a human decision point where the stakes require it.** A type-correct output can
   still be factually wrong.

---

## Skills Learned

- Explain what an API call and an AI coding agent can send to a remote model
- Separate service identity from model identity when making a privacy decision
- Route this course's public filings to direct Anthropic without generalizing that approval
- Read token usage and distinguish cost limits from rate limits
- Design an auditable pipeline with classification, validation, spot checks, and logs

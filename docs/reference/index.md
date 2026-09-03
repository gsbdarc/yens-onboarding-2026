---
layout: default
title: "Reference"
nav_order: 4
has_children: true
has_toc: false
permalink: /reference/
---

# Reference

Two mornings is not enough time for everything in this material. These pages hold
what we could not fit, plus some background reading you may find useful.

Nothing here is assumed in class, and nothing in class depends on it.

---

## Background reading

Optional, and nothing in class depends on them. Useful if you have never worked at a
command line, or want to come back to it afterwards.

| Page | What it covers |
|---|---|
| [Command Line Basics]({{ '/reference/command-line-basics/' | relative_url }}) | `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `rm`; absolute vs. relative paths |
| [Bulk File Operations]({{ '/reference/bulk-file-operations/' | relative_url }}) | Wildcards, pipes, `grep`, `cut`, `sort`, `uniq`, and auditing a data delivery |

## Cut for time

Real topics that did not fit into two mornings. Work through them on your own; the
Slack channel is the place for questions.

| Page | What it covers |
|---|---|
| [Transferring Files (scp)]({{ '/reference/transferring-files/' | relative_url }}) | Copying files between your laptop and the cluster |
| [Exploring Cluster Usage Data]({{ '/reference/cluster-usage-data/' | relative_url }}) | Reading a real Yens monitoring snapshot; per-user vs. whole-node limits |
| [Parallelization Basics]({{ '/reference/parallelization/' | relative_url }}) | When parallelism helps, and the three shapes it takes on a cluster |
| [Documenting Your Pipeline]({{ '/reference/documenting-your-pipeline/' | relative_url }}) | The README that makes a pipeline rerunnable by someone else |

## Going further

Optional, self-serve. Each stands alone — pick one up whenever you like.

| Page | What it covers |
|---|---|
| [LLM-as-a-Judge]({{ '/reference/llm-as-a-judge/' | relative_url }}) | Scale a research judgment call: one model decides, a second checks it, your code routes the contested cases to a human |
| [Why Run LLMs on the Yens?]({{ '/reference/why-local-llms/' | relative_url }}) | Local weights vs. the Gateway vs. a third party; open vs. proprietary models |
| [Running LLMs on the Yens]({{ '/reference/running-llms-on-the-yens/' | relative_url }}) | Query a model running on cluster hardware; GPU tiers and how to ask for one |
| [Handling LLM Failure Modes]({{ '/reference/llm-failure-modes/' | relative_url }}) | Hallucination, inconsistency, and validating output at scale |

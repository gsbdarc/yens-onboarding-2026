---
layout: default
title: "📣 Where to Go Next"
parent: "Part 2 — Scale & Ship"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 4
permalink: /day2/where-to-go-next/
---

# Where to Go Next

Thank you for participating. You are not expected to remember everything from these two
days — you are expected to know where to ask.

---

## Where to Ask

| | Where | For |
|---|---|---|
| 💬 | [**#gsb-yen-users**](https://circlerss.slack.com/archives/C01JXJ6U4E5) on Stanford Slack | Anything about the cluster, Slurm, storage or software. Also where maintenance windows and new hardware get announced. Paste your error output |
| ✉️ | [**gsb_darcresearch@stanford.edu**](mailto:gsb_darcresearch@stanford.edu) | Anything you would rather not post in a channel, or that needs a direct answer. Typically one business day |
| 📖 | [**rcpedia.stanford.edu**](https://rcpedia.stanford.edu) | The written documentation — storage, Slurm, software, quotas, and the current limits |

If the Slack link does not open, search Channels for **#gsb-yen-users** in the app.

{: .note }
> **"Is this dataset OK to send to an LLM?"** is the one question to email rather than post
> — and worth asking before you send, not after.

---

## Keep Going

Everything you ran over these two days is in your fork, and the patterns transfer:

- **More data, same pipeline** — swap the input list in your array script
- **A different model** — change the model name; the rest is identical
- **A new dataset type** — adapt your Pydantic schema and rerun
- **Something that needs a GPU** — see [GPUs]({{ '/day2/gpus/' | relative_url }})

The site stays up. The [Reference]({{ '/reference/' | relative_url }}) section holds what
would not fit into two mornings — including
[Compute Environments]({{ '/reference/compute-environments/' | relative_url }}) and
[Parallelization Basics]({{ '/reference/parallelization/' | relative_url }}), the written
versions of today's two lectures.

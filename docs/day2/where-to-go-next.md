---
layout: default
title: "Where to Go Next"
parent: "Day 2 — The Cluster"
nav_order: 9
permalink: /day2/where-to-go-next/
---

# Where to Go Next

Thank you for participating!

The DARC team runs the Yens and supports GSB researchers year-round. You are not expected to remember everything from these two days — but you are expected to know where to ask.

## Slack — `#gsb-yen-users`

Join the **#gsb-yen-users** channel on Stanford Slack. It's where Yen users and the DARC team:
- Answer questions about the cluster, Slurm, storage, and software
- Share tips and scripts that didn't make it into any tutorial
- Announce workshops, maintenance windows, and new hardware
- Collect feedback about what to improve

**Join here:** [#gsb-yen-users](https://circlerss.slack.com/archives/C01JXJ6U4E5)

If the link does not open automatically, open the Slack app, search for **#gsb-yen-users** in Channels, and join from there.

## Email

For questions that need a direct answer from the team, or anything you'd rather not post in a channel:

**[gsb_darcresearch@stanford.edu](mailto:gsb_darcresearch@stanford.edu)**

Response time is typically one business day.

---

## What to Do When You're Stuck

| Situation | Where to go |
|-----------|-------------|
| "My Slurm job keeps failing" | `#gsb-yen-users` — someone has seen it |
| "Is this dataset ok to send to an LLM?" | Email DARC or ask your IRB coordinator |
| "I want to run something much bigger" | Email DARC — we can advise on allocations |
| "Is there a workshop on X?" | Watch `#gsb-yen-users` for announcements |
| "My code works on my laptop but not the Yens" | `#gsb-yen-users` — include your error output |

---

## Keep Exploring

Everything you ran over these two days is in your fork. Future projects can start from the same patterns:

- **More data, same pipeline:** swap the input list in your Slurm array script
- **Different model:** change `base_url` and `model` — the rest is identical
- **New dataset type:** adapt your Pydantic schema, rerun the pipeline
- **Need a GPU:** add `--gres=gpu:1` (and the GPU partition) to your Slurm script — see [GPUs]({{ '/day2/gpus/' | relative_url }}) and [How to Run LLMs on the Yens]({{ '/reference/running-llms-on-the-yens/' | relative_url }})

The course site stays up, and the [Reference]({{ '/reference/' | relative_url }}) section holds everything we could not fit into two mornings.

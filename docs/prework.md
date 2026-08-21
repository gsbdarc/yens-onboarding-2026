---
layout: default
title: "Before You Arrive"
nav_order: 1
permalink: /prework/
---

# Before You Arrive

This is the checklist version of the **Canvas pre-work module**. Canvas is where you
submit it; this page is here so you have one link to work from.

Budget about an hour. Day 1 starts from the assumption you have done all of it.

---

## 1 — Accounts

| What | Where | Notes |
|---|---|---|
| **Claude** | [uit.stanford.edu/service/claude](https://uit.stanford.edu/service/claude) | Stanford provides Claude for Education free to most people |
| **GitHub** | [github.com/signup](https://github.com/signup) | Free. If you already have one, use it |
| **Yens access** | [Access the Yens](https://rcpedia.stanford.edu/_getting_started/how_access_yens/) | Faculty, PhD students, post-docs, and research fellows have it by default |

{: .warning }
> **Yens access is the one that can take days.** Faculty sponsorship, a SUNet ID, or a
> workgroup addition all involve someone else. Start here, not last.

## 2 — A terminal

- **macOS** — the built-in **Terminal** app. Nothing to install.
- **Windows** — install [Git Bash](https://git-scm.com/downloads) and open it from the Start menu.

## 3 — Confirm your Yens login actually works

The most important item on this list. Submit the output on Canvas.

```bash
ssh SUNetID@yen.stanford.edu
```

Replace `SUNetID` with your Stanford username. Your password will not appear as you
type it — that is normal. You will get a Duo two-factor prompt.

Once you are in, run both of these and paste the commands and their output into Canvas:

```bash
whoami
pwd
```

{: .important }
> If this does not work, **say so on Canvas now**. A login that fails on the morning of
> Day 1 costs you most of Day 1, and it is not something we can fix in the room.

## 4 — Two reading pages, and the quiz

Work through both, doing the exercises rather than just reading. The Canvas quiz draws
directly from them, and Day 1 assumes you can navigate a file system without help.

1. **[Command Line Basics]({{ '/reference/command-line-basics/' | relative_url }})** — `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `rm`, and the difference between an absolute and a relative path. *(~25 min)*
2. **[Bulk File Operations]({{ '/reference/bulk-file-operations/' | relative_url }})** — wildcards, pipes, `grep`, `cut`, `sort`, `uniq`, and how to audit a data delivery for missing files. *(~25 min)*

Then take the **Command line basics** quiz on Canvas. Unlimited attempts — retake it
until you have it all.

---

## What Happens If You Skip This

Nothing punitive. But Day 1 opens at the SSH prompt rather than at `ls`, and the two
mornings are tight enough that we cannot re-teach the pre-work in the room. Somebody who
arrives without it spends Day 1 catching up instead of building the pipeline.

If you are short on time, do items **1 and 3**. Those are the ones that cannot be fixed
on the day.

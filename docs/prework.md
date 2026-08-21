---
layout: default
title: "Before You Arrive"
nav_order: 1
permalink: /prework/
---

# Before You Arrive

This is the checklist version of the **Canvas pre-work module**. Canvas is where you
submit it; this page is here so you have one link to work from.

Budget about **90 minutes**. Day 1 starts from the assumption you have done all of it —
the [dependency map](#what-depends-on-what) at the bottom shows exactly which part of the
course each item unblocks.

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

## 4 — Create a GitHub access token

We push to GitHub from the Yens, and there is no browser there — so you authenticate with
a token instead of a password. Making it takes two minutes in your browser, but doing it
live in class costs the whole room twenty. So do it now.

1. Open this pre-filled link: **[Create your token](https://github.com/settings/tokens/new?scopes=repo,workflow,read:org&description=yen-repo-workflow)**.
   It is a **classic** token, already named `yen-repo-workflow`, with the three scopes you
   need checked: **`repo`**, **`workflow`**, and **`read:org`**.
2. Set the **expiration** to **1 year**.
3. Click **Generate token**, then **copy it immediately** — GitHub shows it only once.
4. Save it somewhere you can get at it on Day 1 — a password manager, or a note on your
   laptop. **Do not** put it in a file inside a git repository.

{: .warning }
> Treat it like a password. If it ever leaks, delete it on GitHub and make a new one.

## 5 — Reading, and the quiz

Work through these, doing the exercises rather than just reading. The Canvas quiz draws
directly from all three.

| # | Read | Time |
|---|---|---|
| a | **[Command Line Basics]({{ '/reference/command-line-basics/' | relative_url }})** — `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `rm`, and absolute vs. relative paths | ~25 min |
| b | **[Bulk File Operations]({{ '/reference/bulk-file-operations/' | relative_url }})** — wildcards, pipes, `grep`, `cut`, `sort`, `uniq`, and auditing a data delivery | ~25 min |
| c | **[Working with Claude Code]({{ '/day1/claude-code/' | relative_url }})** — the pre-read half only: everything from *Meet Claude Code* down to *Claude Code acts as you*. Stop at *In Class*. | ~15 min |

Then take the quiz on Canvas. Unlimited attempts — retake it until you have it all.

{: .note }
> Item (c) is why Claude Code gets a full 25 minutes of hands-on time in class instead of
> a rushed lecture. We will not re-teach the concepts, so the permission modes and the
> data rule won't mean much if you skip it.

---

## What Depends on What

Every item above unblocks something specific. If you are short on time, this is how to
decide what to do first.

| Pre-work item | First needed | Which section | If it's missing |
|---|---|---|---|
| **Yens login works** | Day 1, 9:05 | Connecting to the Yens | **You are blocked from everything.** This cannot be fixed inside a 3-hour morning |
| **Terminal installed** | Day 1, 9:05 | Connecting to the Yens | Same — though fixable in ~5 min if you flag it at 9:00 |
| `pwd`, `ls`, `cd` | Day 1, 9:05 | Connecting to the Yens | You can't navigate cluster storage, and it compounds all morning |
| **Absolute vs. relative paths** | Day 1, 9:20 — and again at 11:10 | Git clone; loading `.env` from `../.env`; running scripts from the repo root | The single biggest source of "file not found" in the whole course |
| **GitHub token** | Day 1, 9:20 | Git & GitHub | The room serialises on token creation — this is measured, not hypothetical |
| GitHub account | Day 1, 9:20 | Git & GitHub | Blocked, but we can create one live in ~2 min |
| **Claude account** | Day 1, 9:33 | Working with Claude Code | Blocked from Claude Code *and* from the capstone's commit step |
| **Claude concepts pre-read** | Day 1, 9:33 | Working with Claude Code | Class is hands-on only; the mode names and the data rule won't mean anything |
| `mkdir`, `cp`, `mv` | Day 1, 10:24 — and again Day 2, 10:10 | Python environments; `mkdir -p logs` before `sbatch` | Slurm resolves `--output` when you submit, so a missing `logs/` fails the job instantly |
| **Wildcards** (`*`) | Day 1, 11:23 — heavily on Day 2 | `ls results/form3_*`, `cat results/*.json`; then `cat logs/extract_*.err` and the `fix_me` debugging | You can't read a failed job's logs or collect your results efficiently |
| **Pipes and `wc -l`** | Day 1, 11:23 | The capstone's `ls results/ \| wc -l` check | You can't quickly answer "did all 10 filings produce a file?" |
| `grep`, `cut`, `sort`, `uniq` | not required in class | — | Nothing is blocked. They appear only in the optional audit exercise |
| `scp` | not required in class | [Reference]({{ '/reference/transferring-files/' | relative_url }}) only | Nothing depends on it — the Yens' shared file system makes it unnecessary |

{: .tip }
> **Short on time?** Do items **1, 3, and 4** — accounts, the login check, and the token.
> Those are the three that cannot be fixed on the day. The reading is catchable; a broken
> login is not.

---

## And After Day 1

There is one assignment **between** the two days: finish the Day 1 capstone and push it.
It is not optional — Day 2 opens by profiling the script you build there, so without it
you cannot do the first hour. Details will be on Canvas.

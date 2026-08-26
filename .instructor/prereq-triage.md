# Day 1, 9:00 — Prereq Triage

**Instructor use only.** Not served by GitHub Pages.

You have **five minutes** at 9:00 to find out who is going to be stuck and do something
about it. This is the order to check, and what to do about each gap.

Pre-work is now **two accounts only** — GitHub, and Claude via Stanford (see
[Before You Arrive](https://gsbdarc.github.io/yens-onboarding-2026/prework/)). Everything
else that used to be pre-work happens in the room, so the triage is shorter but the token
and the terminal are now *your* problem rather than theirs.

---

## Check in this order

Order is by *how unrecoverable the gap is*, not by when it bites.

| # | Check | Blocks from | Verdict if missing |
|---|---|---|---|
| 1 | **Yens login works** | 9:05, everything | **Unrecoverable today.** Do not try to fix it in the room — see below |
| 2 | **Claude account approved** | 9:33 Claude Code, and the capstone's commit step | Hard. ServiceNow approval is not instant. Pair them for the day |
| 3 | **GitHub account exists** | 9:20 Git | Easy — 2 min, let them do it during the welcome |
| 4 | **Terminal opens** | 9:05 | Easy on macOS. Windows without Git Bash needs a ~5 min install — check for Windows laptops early |
| 5 | Shell fluency (`cd`, paths, wildcards) | compounds all morning | **Let this one slide** — see below |

Fastest way to take the reading: ask for a show of hands on 1 and 2 by name. Do not ask
"did everyone do the pre-work?" — you will get a yes.

**The GitHub token is no longer on this list**, because nobody was asked to make one in
advance. It is now created in class at 9:20. See the warning below.

---

## What to actually do

**A broken Yens login is not a Day 1 problem you can solve.** Chasing it is what the
by-name check in `setup.md` is *for*, a week out. If someone still arrives without a working
login: sit them with a partner as a **pair**, one keyboard, and file the access request
during the first break. They will get the concepts and the discussion, and can redo the
hands-on work that evening. This is a much better outcome than losing an instructor for
the morning and still not fixing it.

**No Claude account** is the same shape: pair them. Everything except Claude Code and the
capstone's commit step works without it, and the commit can be done by hand.

**The token is the one thing this pre-work change costs you.** PAT creation was *the*
measured Git bottleneck — moving it to pre-work is why Git & GitHub was budgeted at 13 min
instead of the 20 it ran. It is back in the room now, so **run it as a whole-room step**:
put the pre-filled link on the projector, have everyone open it at once, and wait for the
room. Two minutes done together beats twenty minutes of it happening serially while
everyone else sits idle — which is exactly what happened in the four-day course.

**Shell fluency is the gap to let slide.** It is tempting to re-teach `cd` and relative
paths when you see blank faces, and it is the wrong call: it costs the whole room an hour
you do not have. Pair the person with someone confident, tell
them the [Command Line Basics](https://gsbdarc.github.io/yens-onboarding-2026/reference/command-line-basics/)
page is there for tonight, and keep moving. The one exception worth 30 seconds of whole-room
time is **relative vs. absolute paths**, because it causes more failures across both days
than anything else on the list — a single sentence at 9:05 ("every command today is
relative to your repo root; when a file isn't found, run `pwd` first") pays for itself.

---

## Where each prereq actually bites

Useful when someone asks "do I need this?" — and for deciding what to cut if the room is
weaker than expected.

| Prereq | Used at | In |
|---|---|---|
| Yens login, terminal | D1 9:05 onward | everything |
| `pwd` / `ls` / `cd` | D1 9:05 | Connecting to the Yens |
| Relative vs. absolute paths | D1 9:20, D1 11:10, D2 work block 1 | `git clone`; `load_dotenv("../.env")`; running scripts from the repo root |
| GitHub account | D1 9:20 | `gh auth login` (the token itself is made in class) |
| Claude account + concepts pre-read | D1 9:33 | Working with Claude Code (in-class half) |
| `mkdir` / `cp` / `mv` | D1 10:24, D2 work block 1 | venv creation; `mkdir -p logs` before `sbatch` |
| Wildcards (`*`) | D1 11:23, D2 work blocks 1–2 | `ls results/form3_*`, `cat results/*.json`; `cat logs/extract_*.err`, `cat logs/fix_me_*.err` |
| Pipes, `wc -l` | D1 11:23 | the capstone's `ls results/ \| wc -l` completeness check |
| `grep`, `cut`, `sort`, `uniq` | **never in class** | the optional Reference audit exercise only |
| `scp` | **never in class** | Reference page only |

Note what is *not* on this list: `grep` and the `cut`/`sort`/`uniq` pipeline appear only in
the optional Reference reading and are never required in class, and `squeue` filtering uses
its own flags
(`--me`, `-p`, `-o`) rather than pipes. Don't let a weak-on-`grep` room worry you.

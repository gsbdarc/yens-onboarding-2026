# Day 1 — Teaching Run-of-Show (9:00–12:00)

**Instructor use only.** Not served by GitHub Pages. See `docs/agenda.md` for the
section table; this is how to run it.

3 hours including two 10-minute breaks → ~160 min of teaching. Blocks around the breaks
are ≈ **60 / 50 / 50**.

## How to run it

- **Drive each section live on screen.** Pause at the end of each for stragglers before
  moving on.
- **Optional practice is the buffer.** Point fast finishers at it rather than slowing the
  whole room.
- **The pre-work is doing real work here.** Day 1 opens at SSH, not at `ls`. If several
  people clearly have not done it, do *not* re-teach the CLI — seat a helper with them
  and keep the room moving.

## Where the time actually goes

| Section | Watch out for |
|---|---|
| Connecting to the Yens (20) | Duo prompts and first-login banners eat time. Have the SSH multiplexing tip ready for anyone re-authenticating repeatedly. |
| Git & GitHub (15) | The PAT step is the bottleneck — token creation happens in a browser on their laptop while `gh auth login` waits on the Yens. Put the pre-filled token link on screen and leave it there. |
| Claude Code (15) | First-run SUNet sign-in can stall. This section is trimmed hard from the original 441-line page; teach models, permission modes, and the data rule, then one real task. Skip the tokens/context deep dive unless asked. |
| Running Python (15) | The `$PATH` demo is the point; JupyterHub is a tour, not a lab. Cut the notebook-editing bit first if you're behind. |
| Python Environments (20) | **Protected.** The Potion Brawl rebuild is what makes reproducibility land. If short, demo it on screen rather than dropping it. |
| Stanford's AI Services (15) | Mostly discussion. The data-risk table is the one thing everyone must leave with. |
| API Keys (10) | Brisk. The "a committed key is a leaked key" point is worth the whole 10 minutes. |
| Extracting Data with an LLM (25) | **Protected.** The three staged scripts exist so the diff between them *is* the lesson — walk `diff step2 one_file` on screen. |
| Capstone + privacy discussion (15) | Start the 10-filing run first, then discuss while it executes. |

## If you are running behind at 11:10

In order: drop the notebook-editing part of Running Python, then demo rather than
run the Potion Brawl rebuild, then trim the Day 1 capstone's "What to Look For" to a
single question asked aloud. **Do not cut the Pydantic validation step** — Day 2's
profiling and Slurm sections both assume a working `extract_form_3_batch.py`.

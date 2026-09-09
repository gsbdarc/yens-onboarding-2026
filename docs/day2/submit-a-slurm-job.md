---
layout: default
title: "3. Submit"
parent: "Part 1 — Profile & Submit a Job"
grand_parent: "Day 2 — The Yen-Slurm Cluster"
nav_order: 3
permalink: /day2/submit-a-slurm-job/
---

# Submit

{: .note }
> 🟢 **Green sticky** = I'm done and ready &nbsp;&nbsp; 🔴 **Red sticky** = I need help
>
> Put one up as soon as either is true — an instructor will come to you.

<svg viewBox="0 0 720 164" role="img" aria-labelledby="daymap-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:720px;height:auto;margin:1.5rem auto" font-family="'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="daymap-title">Day 2 arc — you are on step 3, submit.</title>
  <defs>
    <marker id="daymap-ah" markerWidth="9" markerHeight="9" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="#c2cad4"/></marker>
  </defs>
  <text x="70" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">profile</text>
  <text x="210" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">document</text>
  <text x="350" y="46" text-anchor="middle" font-size="17" font-weight="700" fill="#8C1515">submit</text>
  <text x="490" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">read logs</text>
  <text x="630" y="46" text-anchor="middle" font-size="17" font-weight="400" fill="#6a7280">scale (Part 2)</text>
  <line x1="92" y1="80" x2="608" y2="80" stroke="#c2cad4" stroke-width="3"/>
  <path d="M490,101 L490,124 Q490,130 484,130 L356,130 Q350,130 350,124 L350,103" fill="none" stroke="#c2cad4" stroke-width="2.5" stroke-dasharray="5 4" marker-end="url(#daymap-ah)"/>
  <text x="420" y="150" text-anchor="middle" font-size="15" font-weight="400" fill="#6a7280">debug</text>
  <circle cx="70" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="70" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">1</text>
  <circle cx="210" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="210" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">2</text>
  <circle cx="350" cy="80" r="20" fill="#fff" stroke="#8C1515" stroke-width="3"/><text x="350" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#8C1515">3</text>
  <circle cx="490" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="490" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">4</text>
  <circle cx="630" cy="80" r="20" fill="#f3f4f7" stroke="#6a7280" stroke-width="3"/><text x="630" y="87" text-anchor="middle" font-size="20" font-weight="700" fill="#6a7280">5</text>
</svg>

{: .note }
> Everything on this page runs from your clone, with the environment active:
>
> ```bash
> cd ~/yens-onboarding-2026
> source .venv/bin/activate
> ```

---

## Read the Queue First

Before you add a job to the queue, look at the queue.

{: .important }
> **Task:** Look at the live Slurm queue to see what jobs are waiting or running right now.

```bash
squeue
```

Look at the columns:
- **JOBID** — unique ID for each job
- **PARTITION** — which partition (queue) the job was submitted to — each partition has different node types, time limits, and resource caps; see the [current partitions and their limits](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits)
- **ST** — status: `R` = running, `PD` = pending (waiting in queue for resources)
- **TIME** — how long the job has been running
- **NODELIST** — which compute node it landed on

There is also a shorthand to filter to just your jobs:

```bash
squeue --me
```

You can also filter by partition — for example, to see only GPU jobs:

```bash
squeue -p gpu
```

Every `PD` job is waiting for a node with the resources it requested. When Slurm finds a matching node — it runs.

Now run `sinfo` to see the state of all nodes and the partitions they belong to:

```bash
sinfo
```

- How many compute nodes are currently idle (`STATE=idle`)?
- What partitions exist? Which one would you use for a normal job?
- What is the maximum time limit for each partition? See the
  [current partitions and their limits](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits).

---

## Write and Submit a Job

{: .important }
> **Task:** Build a Slurm job script line by line to run your Form 3 extraction script on a compute node.

**Start from a clean shell.** If you have a virtual environment active right now (you'll see `(.venv)` at the front of your prompt), deactivate it first:

```bash
deactivate
```

`sbatch` copies your current shell's environment into the job by default, so if `.venv` is active when you submit, it **rides along** — and the job can quietly succeed even if the script forgot to activate it. Deactivate first so the job runs on only what the **script** sets up (the `source .venv/bin/activate` in Step 3) — the way it'll run for a teammate, or for you from a clean login.

**Create the file:**

Your repo already has a `slurm/` folder (with a few prepared scripts). Just make sure a `logs/` folder exists for job output:

```bash
mkdir -p logs
```

{: .warning }
> **The `logs/` folder must exist before you submit.** Slurm opens your `--output`/`--error` files the moment the job starts — it does **not** create missing directories. If you point `--output` at `logs/…` but there's no `logs/` folder, the job **fails silently**: nothing runs and no log file appears to tell you why. Create it once, up front. (If instead you point `--output` at a bare `extract.out` with no folder, the file lands in whatever directory you ran `sbatch` from.)

Create a new file `slurm/extract_form_3_batch.slurm` and open it in your editor — you'll build it up line by line below.

{: .note }
> No preferred terminal editor? You can create it right in **JupyterHub**: in the file browser, open the `slurm/` folder, click **+ New → Text File** (or **File → New → Text File**), edit it in the browser, then **rename** the file to `extract_form_3_batch.slurm` and save with `Cmd/Ctrl+S`.

---

**Step 1 — The shebang**

The first line of every shell script is the **shebang**:

```bash
#!/bin/bash
```

The `#!` (the **shebang**) tells the operating system which **interpreter** — the program that reads your script and runs it line by line — to use for the rest of the file; here, the Bash shell at `/bin/bash`. Without it, the system doesn't know whether your script is Bash, Python, or something else. It has to be the very first line of the file.

---

**Step 2 — SBATCH directives**

These are instructions to the Slurm scheduler — add them at the top of the file, right after the shebang:

```bash
#SBATCH --job-name=<job-name>
#SBATCH --partition=normal
#SBATCH --output=logs/extract_%j.out
#SBATCH --error=logs/extract_%j.err
#SBATCH --time=<HH:MM:SS>
#SBATCH --mem=<RAM>
#SBATCH --cpus-per-task=<cores>
```

What each one is:

- `--job-name` — a short label **you pick** so you can spot this job in the queue (e.g. `form3-extract`). It doesn't affect resources; name it whatever's memorable.
- `--partition` — the queue the job runs in. `normal` is the production partition; each partition has its own time limits and resource caps (see the [current partitions and their limits](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits)).
- `--output` / `--error` — files where the job's normal output and errors get written; `%j` is auto-filled with the job ID, so each run gets its own log. **Leave these as-is.**
- `--time`, `--mem`, `--cpus-per-task` — the resources you're **requesting**. Fill these in from the **time**, **RAM**, and **CPU cores** you recorded in your Profiling README.

{: .note }
> **About the `--output` and `--error` files:**
> - A batch job has **no terminal** — you're not watching it run. So Slurm redirects everything your script would normally print: normal output goes to the **`--output` (`.out`) file**, and error messages/tracebacks go to the **`--error` (`.err`) file**. Those files are how you see what the job did and debug it when it fails.
> - `%j` gets replaced with the job ID, so each run writes its own `logs/extract_JOBID.out` and `.err` instead of overwriting the last.
> - **Combine them if you like:** omit `--error` entirely and Slurm sends *both* normal output and errors to the single `--output` (`.out`) file. Keeping them separate just makes errors easier to spot.
> - The `logs/` directory must exist before the job runs — Slurm won't create it, which is why `mkdir -p logs` came first.

---

**Step 3 — Set up the environment**

```bash
# Navigate to your project
cd $HOME/yens-onboarding-2026

# Activate your virtual environment
source .venv/bin/activate
```

{: .note }
> **What's already installed.** Your `.venv` was built from `requirements.txt` on Day 1. Once it's activated, any job can use these packages:
>
> | Package | Used for |
> |---|---|
> | `anthropic` | Calling the Anthropic API (LLM extraction) |
> | `python-dotenv` | Loading your API key from `.env` |
> | `pydantic` | Validating and structuring the LLM output |
> | `pandas` | Tabular data |
> | `numpy` | Vectorized numerics (installed with pandas) |
> | `requests` | Downloading filings over HTTP |
> | `ipykernel` / `jupyter` | Notebook and JupyterHub kernels |
> | `matplotlib` | Plots |
>
> Need something else? `pip install` it into your `.venv` (never system-wide) and add it to `requirements.txt` so your work stays reproducible.

---

**Step 4 — Add the line that runs your script**

The last line of the file is the actual work — the command Slurm will run on the compute node when the job starts. It's a line you write *inside* the script, **not** something you run yourself right now:

```bash
python scripts/extract_form_3_batch.py
```

This runs the **10-filing batch you profiled** — `scripts/extract_form_3_batch.py` loops over `NUM_FILINGS` (10) SEC Form 3 filings from `data/aws_links.csv` — so the `--time`, `--mem`, and `--cpus-per-task` you filled in above come straight from your Profiling README.

Save the file. Here's the whole script, with its four parts labeled:

<svg viewBox="0 0 700 292" role="img" aria-labelledby="anatomy-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:700px;height:auto;margin:1.5rem auto" font-family="'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="anatomy-title">The anatomy of a Slurm batch script: the shebang, the #SBATCH resource directives, the environment setup, and the run line(s) that do the work.</title>
  <rect x="16" y="10" width="440" height="272" rx="10" fill="#fbfcfe" stroke="#d5d8e2" stroke-width="1.5"/>
  <rect x="18" y="22" width="436" height="22" fill="#f3f4f7"/>
  <rect x="18" y="58" width="436" height="144" fill="#fdf0e3"/>
  <rect x="18" y="214" width="436" height="44" fill="#eaf1fb"/>
  <rect x="18" y="260" width="436" height="22" fill="#e9f5ee"/>
  <g font-family="'Source Code Pro', ui-monospace, SFMono-Regular, Menlo, monospace" font-size="13" fill="#5b6472">
    <text x="32" y="38">#!/bin/bash</text>
    <text x="32" y="76">#SBATCH --job-name=&lt;job-name&gt;</text>
    <text x="32" y="96">#SBATCH --partition=normal</text>
    <text x="32" y="116">#SBATCH --output=logs/extract_%j.out</text>
    <text x="32" y="136">#SBATCH --error=logs/extract_%j.err</text>
    <text x="32" y="156">#SBATCH --time=&lt;HH:MM:SS&gt;</text>
    <text x="32" y="176">#SBATCH --mem=&lt;RAM&gt;</text>
    <text x="32" y="196">#SBATCH --cpus-per-task=&lt;cores&gt;</text>
    <text x="32" y="232">cd $HOME/yens-onboarding-2026</text>
    <text x="32" y="252">source .venv/bin/activate</text>
    <text x="32" y="276">python scripts/extract_form_3_batch.py</text>
  </g>
  <circle cx="472" cy="33" r="6" fill="#8a94a6"/><text x="486" y="38" font-size="13.5" font-weight="700" fill="#2c3e50">shebang — the interpreter</text>
  <circle cx="472" cy="130" r="6" fill="#e67e22"/><text x="486" y="126" font-size="13.5" font-weight="700" fill="#2c3e50">#SBATCH — requests to the</text><text x="486" y="145" font-size="12.5" fill="#6a7280">scheduler (not commands)</text>
  <circle cx="472" cy="236" r="6" fill="#2f6fb0"/><text x="486" y="232" font-size="13.5" font-weight="700" fill="#2c3e50">environment setup —</text><text x="486" y="251" font-size="12.5" fill="#6a7280">cd + activate venv, on the node</text>
  <circle cx="472" cy="276" r="6" fill="#2e8b57"/><text x="486" y="280" font-size="13.5" font-weight="700" fill="#2c3e50">run line(s) — your command(s)</text>
</svg>

*Every Slurm script has these four parts: the **shebang**, the **`#SBATCH`** directives (requests to the scheduler, not commands that run), the **environment setup** that runs on the compute node, and the **run line(s)** that do the actual work.*

{: .warning }
> **Slurm starts a fresh shell on the compute node.** Your virtual environment is not active. Your working directory is not set. Every setup step must be in the script — `cd`, `source .venv/bin/activate`, and any `module load` commands you need. If it works interactively on the Yens but fails as a job, a missing setup step is usually why.

---
### Submit it

{: .important }
> **Today only:** this class has a dedicated Slurm reservation, `class_day2`. Add `--reservation=class_day2` to every `sbatch` (and `srun`) command today so your jobs run on the reserved nodes. It's a class-day flag — drop it for your own work after today.

```bash
sbatch --reservation=class_day2 \
  slurm/extract_form_3_batch.slurm
# Submitted batch job 12345678
```

Monitor the queue:

```bash
squeue --me
```

---

### Cancel it

```bash
scancel JOBID
```

Replace `JOBID` with your job's actual number — the one `sbatch` printed (`Submitted batch job 12345678`) and that shows in `squeue --me`. It's not the literal word `JOBID`.

Confirm it is gone:

```bash
squeue --me
```

{: .note }
> You may briefly see your job's status change to **CG** (completing) before it disappears from the queue — that's normal, not an error.

---

### Add email notifications

**Ask Claude Code to add** the two email directives to your script — these two lines:

```bash
#SBATCH --mail-type=ALL
#SBATCH --mail-user=SUNetID@stanford.edu
```

<details markdown="1">
<summary>💡 Hint — a prompt to try</summary>

> Add `--mail-type=ALL` and `--mail-user=SUNetID@stanford.edu` to the `#SBATCH` directives in `slurm/extract_form_3_batch.slurm`.

</details>

`ALL` sends an email when the job starts, ends, and fails — including a utilization summary showing how much CPU and RAM it actually used.

Resubmit:

```bash
sbatch --reservation=class_day2 \
  slurm/extract_form_3_batch.slurm
```

Once your job runs, check your inbox. You should receive two emails: one when the job **starts** and one when it **ends**. The start email tells you when it began — compare that to when you submitted to see how long it **waited in the queue**. The end email includes a **utilization summary** (how much CPU time and memory the job actually used) and the job's **exit status**: `0` means success; any other value means it failed.

### Read the logs

The job wrote **log files** to `logs/` — the `.out` file has the script's normal output, the `.err` file has any errors:

```bash
cat logs/extract_*.out
cat logs/extract_*.err
```

---

<details markdown="1">
<summary>⭐ Bonus — if you finished early</summary>

**Bonus — Go Interactive Instead of Batch**

Everything so far has been batch submission — write a script, `sbatch` it, wait. Slurm also supports an interactive allocation on a dedicated node — handy when you're debugging and re-running over and over: you hold the allocation, so you don't re-queue for resources every time a job fails and you fix it:

```bash
srun --reservation=class_day2 --pty --cpus-per-task=2 --mem=4G --time=00:30:00 bash
```

Your interactive session is a Slurm job like any other — run `squeue --me` and you'll see it listed (state `R`) until you release it:

```bash
squeue --me
```

Once it drops you into a shell on your allocated node, you're on a fresh shell — do the same setup your batch script does, then run the script directly:

```bash
cd $HOME/yens-onboarding-2026   # into your project
source .venv/bin/activate                   # activate your environment
python scripts/extract_form_3_batch.py   # run it and watch the output live
```

Because you're interactive, you see the output as it happens and can re-run instantly after a fix — no re-queuing. Type `exit` to release the allocation when you're done.

**Bonus — Watch a Job Run on Its Node**

`slurm/mystery.slurm` runs the mystery script from Profiling for about **30 seconds** across a few cores — long enough to watch it live.

Submit it:

```bash
sbatch --reservation=class_day2 slurm/mystery.slurm
```

While your job is running you can SSH to the node it's on and watch it work. (Nodes are **shared** — other users' jobs run on them too — but your job has its own **dedicated cores and RAM**.)

First, run `squeue --me` to find which node it landed on — the `NODELIST` column (e.g. `yen10`):

```bash
squeue --me
```

Then SSH to that node and watch your processes live:

```bash
ssh SUNetID@yen10   # use your job's actual node
htop -u SUNetID                  # or: top -u SUNetID
```

You'll see the mystery script's Python workers pinning the cores you requested. Press `q` to quit `htop`, then `exit` to leave the node.

{: .note }
> You can only SSH to a compute node **while you have a job running on it** — once the job ends (or if you never had one there), SSH to that node is refused. You can't hop onto arbitrary compute nodes.

**Bonus — Chain Two Jobs**

A real research pipeline is a chain of **stages**, each feeding the next. Scaled up, your Form 3 work is naturally three jobs: **(1) download** the raw filings from EDGAR, **(2) extract** the structured fields with the API (what your batch script does), then **(3) aggregate** the per-filing JSON into one dataset and compute summary stats. Each stage reads the file the one before it wrote — stage 2 can't start until stage 1's downloads land, and stage 3 needs stage 2's extractions. Rather than babysit them, launching each by hand the moment the last finishes, you queue the whole chain at once: `--dependency=afterok` tells Slurm to hold each job until the one before it **succeeds**. Your repo ships a small two-step version of this:

- `scripts/chain_step1.py` — crunches numbers for ~2 minutes, then writes its result to `/scratch/users/SUNetID/chain_demo/step1_result.txt`.
- `scripts/chain_step2.py` — reads that file and does ~30 seconds more math, writing `step2_result.txt` beside it.

with `slurm/chain_step1.slurm` and `slurm/chain_step2.slurm` to run them.

**Step 1 — read both job scripts first** so you know what you're submitting. Notice they're ordinary Slurm scripts, and that step 2 reads the file step 1 wrote:

```bash
cat slurm/chain_step1.slurm slurm/chain_step2.slurm
```

**Step 2 — have Claude add the email lines to step 2** *before* you submit, so you get a note when the chain finishes:

> Add `#SBATCH --mail-type=ALL` and `#SBATCH --mail-user=SUNetID@stanford.edu` to `slurm/chain_step2.slurm`.

**Step 3 — submit both back-to-back.** Step 1 runs for ~2 minutes, so fire them off one after the other and let it crunch while step 2 queues behind it. Submit step 1 and note the `JOBID` it prints:

```bash
sbatch --reservation=class_day2 slurm/chain_step1.slurm
```

Then submit step 2 right away, chained to the first — replace `JOBID` with step 1's ID:

```bash
sbatch --reservation=class_day2 --dependency=afterok:JOBID slurm/chain_step2.slurm
```

**Step 4 — watch the queue.** Both jobs are in, but step 2 waits its turn. `watch` re-runs a command every couple of seconds, so you can see the handoff happen live:

```bash
watch squeue --me
```

Step 1 shows `R` (running) while step 2 sits `PD` with reason `(Dependency)`. When step 1 finishes, step 2 flips to `R` on its own — you do nothing. Press `Ctrl-C` to stop watching.

{: .note }
> 💡 If step 1 **fails**, `afterok` is never satisfied, so step 2's reason in `squeue` changes from `(Dependency)` to `(DependencyNeverSatisfied)`. That job will never run — but it won't clear itself either. It sits in the queue until **you** cancel it with `scancel JOBID`. Clear it, fix step 1, then requeue the chain.

**Step 5 — check the handoff** once both are done:

```bash
cat /scratch/users/SUNetID/chain_demo/step2_result.txt
```

Step 2's number is computed from step 1's — proof the scratch file passed between them. Had step 1 failed, step 2 would never have started.

**Bonus — The `dev` partition**

The Yens have a dedicated **`dev` partition** for short, interactive debugging jobs — quick test runs while you're getting a script working, **not** production runs. It has tighter time limits but is meant to turn around fast, so you're not stuck in the main queue while iterating. Learn more: [Yen Slurm partitions](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits).

<details markdown="1">
<summary>📋 Show steps</summary>

Fire a quick throwaway job at `dev` with `-p dev` (and `--wrap`, which runs an inline command as a job). It's tiny, so it schedules fast, and it emails you when it finishes:

```bash
sbatch --reservation=class_day2 -p dev --mail-type=ALL --mail-user=SUNetID@stanford.edu --wrap="hostname; sleep 30"
```

Watch it — `dev` usually starts right away:

```bash
squeue --me
```

You'll get a completion email in a moment. Confirm it says the job completed.

</details>


**Bonus — Add a `longsqueue` alias**

The default `squeue` output is sparse. Pass a custom format to see what each job actually
requested — CPU cores, memory, and time limit:

```bash
squeue -o "%.18i %.9P %.8j %.8u %.8T %.10M %.10l %.4C %.7m %.15R"
```

The columns are: job ID, partition, job name, user, state, time elapsed, time limit, CPU
cores requested, memory requested, and reason/node.

To keep it, append an alias. The quoted heredoc (`<<'EOF'`) means nothing inside needs
escaping — paste the whole block at once:

```bash
cat >> ~/.bash_profile <<'EOF'
alias longsqueue='squeue -o "%.18i %.9P %.8j %.8u %.8T %.10M %.10l %.4C %.7m %.15R"'
EOF
source ~/.bash_profile
```

Now run `longsqueue`. If the alias comes back "not found", check the tail of the file with
`tail -3 ~/.bash_profile` before appending again.

**Bonus — Inspect any job with `scontrol`**

Pick any job from `squeue` and look up its full details:

```bash
scontrol show job JOBID
```

Find **NumCPUs** (cores requested), **mem=** (RAM requested) and **TimeLimit**. This works
on any job — yours or someone else's — as long as it is still queued or running.

**Bonus — Compare partitions**

Run `sinfo -p gpu` and `sinfo -p normal` to compare node counts and time limits. `sinfo`
does not show the per-user resource **caps** — those come from each partition's QoS, so
check `sacctmgr show qos gpu` against `sacctmgr show qos normal` (or the
[current partitions and their limits](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits)).
When would you request one over the other?
</details>

---

<details markdown="1">
<summary>⭐ Bonus — turn this into a Claude skill</summary>

You just wrote a Slurm script by hand and got it working. That working setup is the raw
material for a **skill**, and this page distills two of them from it — one for how the Yens
work, one for how this project does things.

You are the reviewer throughout: you submit and check the work, not Claude.

### Two homes for a skill

Every skill is a **directory** holding one file named exactly `SKILL.md`. The directory
name is the skill's name — lowercase letters, digits and hyphens only — and it is also how
you invoke it: `form3-plots/` gives you the `/form3-plots` command.

Where the directory lives decides its scope:

- **Global skill** → `~/.claude/skills/<skill-name>/SKILL.md` — in your **home** directory (`~/.claude/`), so it loads in *every* project you work on. That's where the Day 1 skill lives. Best for **conventions that follow you** across projects (like how the Yens work).
- **Project skill** → `<your-repo>/.claude/skills/<skill-name>/SKILL.md` — in the **repo's own** `.claude/` (no `~/`), so it loads only in *this* repo and, once committed, ships to anyone who clones it. Best for **repo-specific** conventions (how this project makes figures, where results land, which script to run).

<svg viewBox="0 0 700 196" role="img" aria-labelledby="scope-title" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;max-width:700px;height:auto;margin:1.5rem auto" font-family="'Source Sans 3', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">
  <title id="scope-title">A global skill lives in your home ~/.claude/ and loads in every project; a project skill lives in the repo's own .claude/ and ships to anyone who clones it.</title>
  <rect x="16" y="8" width="330" height="180" rx="12" fill="#eef5ff" stroke="#bcd4f2" stroke-width="1.5"/>
  <text x="34" y="36" font-size="16" font-weight="700" fill="#2c3e50">🌐  GLOBAL skill</text>
  <text x="34" y="58" font-size="12.5" fill="#6a7280">~/.claude/ · your home directory</text>
  <g font-family="'Source Code Pro', ui-monospace, SFMono-Regular, Menlo, monospace" font-size="13" fill="#5b6472">
    <text x="34" y="90">~/</text>
    <text x="34" y="112">└─ .claude/skills/</text>
    <text x="34" y="134">      └─ yen-slurm/</text>
    <text x="34" y="156">            └─ SKILL.md</text>
  </g>
  <text x="34" y="180" font-size="13" font-weight="700" fill="#b3611a">loads in EVERY project — follows you</text>
  <rect x="354" y="8" width="330" height="180" rx="12" fill="#fff8ef" stroke="#e6cfa8" stroke-width="1.5"/>
  <text x="372" y="36" font-size="16" font-weight="700" fill="#2c3e50">📦  PROJECT skill</text>
  <text x="372" y="58" font-size="12.5" fill="#6a7280">the repo's own .claude/ (no ~/)</text>
  <g font-family="'Source Code Pro', ui-monospace, SFMono-Regular, Menlo, monospace" font-size="13" fill="#5b6472">
    <text x="372" y="90">yens-onboarding-2026/</text>
    <text x="372" y="112">└─ .claude/skills/</text>
    <text x="372" y="134">      └─ form3-plots/</text>
    <text x="372" y="156">            └─ SKILL.md</text>
  </g>
  <text x="372" y="180" font-size="13" font-weight="700" fill="#b3611a">loads only in THIS repo — ships on clone</text>
</svg>

*Same `.claude/skills/` layout, two different homes: the **global** skill in `~/.claude/` follows you into every project; the **project** skill in the repo's `.claude/` is committed and ships to anyone who clones it.*

You'll write the global one first, then the project one.

### Write a Global Skill

{: .important }
> **Task:** Have Claude distill a **global** Yen skill from the Slurm job you just ran by hand, then invoke it on a fresh job.
>
> Work through this at your own pace. The point is the *pattern* — do the work, then distill
> it into a skill — so if you only get as far as reading the `SKILL.md` Claude writes, you
> have got the idea.

You'll do this from Claude Code running on the Yens. Load the module and launch it inside your repo:

```bash
ml claude-code
cd ~/yens-onboarding-2026
claude
```

#### A global skill — distilled from the job you just ran

You already got a batch Slurm script working by hand. Rather than describe the Yen conventions from scratch, point Claude at that script and have it **capture the reusable parts** (step 2 of the pattern):

> Read `slurm/extract_form_3_batch.slurm` and turn its reusable **Yen conventions** into a **global** skill at `~/.claude/skills/yen-slurm/SKILL.md`: partition choice, email, `%j` log naming, always setting `--time`/`--mem`/`--cpus-per-task`, and checking current limits on [RCpedia](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits). Keep it short and **repo-agnostic** — no project paths.

**Check what it wrote.** A good skill is short, and its **`description`** is what makes Claude reach for it later — so open the file and read it:

```bash
cat ~/.claude/skills/yen-slurm/SKILL.md
```

It should look something like this — a little frontmatter, then a few bullet conventions:

```markdown
# ~/.claude/skills/yen-slurm/SKILL.md
---
name: yen-slurm
description: Write and check Slurm batch scripts for Stanford's Yen cluster — partitions, email, %j logs, resource requests. Use when writing a .slurm job.
---

When writing a Yen job script:
- Choose a partition: `normal` for production, `dev` for short jobs (limits on RCpedia)
- Always set `--time`, `--mem`, and `--cpus-per-task`
- Email on completion: `--mail-type=ALL`, `--mail-user=SUNetID@stanford.edu`
- Name logs `logs/<job-name>_%j.out` and `.err`
```

The **`description` is the trigger** — Claude reads it to decide when to pull the skill in. Leave it vague ("slurm stuff") and it won't fire when you need it; say what it does *and when to use it*.

Then invoke it (step 3) on a fresh job. Claude Code turns each skill's folder name into a `/`-command, so the `yen-slurm/` folder gives you `/yen-slurm` — type it and add your request:

> /yen-slurm write a Slurm job for a new run and save it as `slurm/extract_form_3_batch_claude.slurm`

**Submit and review:** the conventions should come straight from the skill, matching what you hand-wrote. But the global skill is repo-agnostic — it says nothing about *how this project plots a figure*. That's project-specific knowledge, and it belongs in a project skill — the next section.

### Write a Project Skill — Your Figure House Style

Skills shine when Claude follows *your* world's conventions instead of generic defaults — a house style so every figure comes out consistent.

**Step 1 — work with Claude until the figure looks right.** Ask it to make and run a small plotting job:

> Write `scripts/plot_letter_distribution.py` that reads every JSON in `results/` and counts how often each letter a–z appears across all the extracted text fields (`insider_name`, `company_name`, and the roles). Save a bar chart to a new `figures/` directory (`figures/letter_distribution.png`), creating the directory if it doesn't exist. Use our Stanford palette: cardinal-red (`#8C1515`) bars, Stanford-black (`#2E2D29`) title and axis labels, white background. Then write `slurm/plot.slurm` to run it on the `dev` partition, and submit it with today's class reservation: `sbatch --reservation=class_day2 slurm/plot.slurm`.

Iterate with Claude on colours, title, and axis labels until you like it. (Open `figures/letter_distribution.png` in JupyterHub to see it.)

{: .note }
> 💡 **Example prompts to iterate with Claude** — you don't need to know matplotlib, just describe the look:
> - Make every other bar a lighter cardinal shade (`#B83A4B`) so adjacent bars are easy to tell apart.
> - Add a title "Letter frequency across 10 Form 3 filings" and label the axes ("Letter" on x, "Count" on y).
> - Sort the bars from most to least frequent instead of alphabetical.
> - Bump the figure size and dpi so it's readable in a slide, and add light gridlines.

**Step 2 — distill the style into a skill.** This one is a **project** skill, so it goes in **this repo's own `.claude/`** — *not* your home `~/.claude/` — so it ships with the project to anyone who clones it. Once you're happy with how the figure looks:

> Turn the plotting style we just settled on into a **project** skill in **this repo** at `./.claude/skills/form3-plots/SKILL.md` (the repo's `.claude/`, not `~/.claude/`) — this repo's figure house style: the Stanford palette (cardinal `#8C1515` bars, `#2E2D29` text), figure size, dpi, axis-label conventions, and that PNGs save to `figures/`. Keep it to *this* project.

**Step 3 — invoke it on a *different* plot** to prove it fires. Either just describe the task and let the skill's `description` trigger it automatically, or call it explicitly with `/form3-plots` — no style instructions either way:

> /form3-plots plot the distribution of insider roles across the 10 filings

It should come out in the same house style automatically — that's the skill doing its job.

**Takeaway:** the global skill knows *how the Yens work* — it lives in your home `~/.claude/`, so it follows *you* to every project. The project skill knows *how this project does things* — it lives in the repo's own `.claude/` (no `~/`), so committing it ships the skill to anyone who clones. Both come from work you already did right — you just asked Claude to remember it.

{: .warning }
> **You're still the reviewer.** A skill makes Claude follow your conventions, but Claude can still invent partition names, time limits, or QoS caps that don't exist. Check its choices against RCpedia — the [current partitions and their limits](https://rcpedia.stanford.edu/_user_guide/slurm/#current-partitions-and-their-limits) page and `sacctmgr show qos <partition>` — and against your own profiling. The script you submit is yours.

---

### Claude in One Shot

*Print mode — `claude -p`.*

Everything above used Claude Code **interactively**. For a quick, one-off question — or to script it — Claude also runs **non-interactively**: `claude -p "…"` (print mode) runs a single prompt, prints the answer, and exits. No session, no back-and-forth.

Point it at a file — e.g. review one of the broken scripts from the [**Read Logs** exercise]({{ '/day2/debug-a-failed-job/' | relative_url }}):

```bash
claude -p "review scripts/extract_form_3_one_file_broken.py and explain what it does"
```

Or **pipe** data straight into it. On Linux, every command-line program has two text streams: **standard input** (`stdin`, the text coming *in*) and **standard output** (`stdout`, the text it prints *out*). The pipe symbol `|` connects them — it takes the `stdout` of the command on its left and feeds it as the `stdin` of the command on its right. Because `claude -p` reads from `stdin`, you can pipe a file's contents straight into Claude instead of typing them. Take a failed job's error log from the [**Read Logs** exercise]({{ '/day2/debug-a-failed-job/' | relative_url }}) (run those first, so the `logs/fix_me_*.err` files exist) and let Claude diagnose it in one line:

```bash
cat logs/fix_me_*.err | claude -p "this Slurm job failed — explain the error and suggest a fix"
```

Because it's just another command that reads `stdin` and prints to `stdout`, you can drop `claude -p` **inside a Slurm job or a shell script** and let it work in **batch mode** — no interactive session at all.

Picture inheriting a whole project you didn't write — a stack of scripts and Slurm jobs. You can wire `claude -p` into those jobs so that, as each one runs unattended, Claude documents the run for you: at the end of the script, pipe the results (or the log) to Claude and have it append a plain-English summary of what ran, what the output means, and anything that looks off — straight into the job's own output. For example, add a few lines to the *end* of a `.slurm` script, after the real work:

```bash
# ... your extraction / analysis commands above ...

# Let Claude write a human-readable summary of this run into the log
cat results/*.json \
  | claude -p "Summarize what this run produced and flag anything unusual." \
  >> logs/run_summary.txt
```

Submit a batch of these and you come back to finished jobs that have already **documented themselves** — what they did, when, and what to look at — without you watching a single one run.

</details>

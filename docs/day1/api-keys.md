---
layout: default
title: "Managing API Keys"
parent: "Part 2 — Python & AI"
grand_parent: "Day 1 — Foundations & AI"
nav_order: 5
permalink: /day1/api-keys/
---

# Managing API Keys

An API key is a credential. Anyone holding it can use the service and spend its budget,
so it must not appear in source code, Git history, notebook output, screenshots, chat, or
logs. You will copy the course's Anthropic key into a local `.env`, prove that Git ignores
it, and initialize the client without ever displaying the secret.

---

## Exercise

{: .important }
> **In this section:** Load `ANTHROPIC_API_KEY` from `.env`, verify the variable without
> revealing its value, confirm `.env` is ignored by Git, and initialize Anthropic's native
> Python client.

## Step 1: Keep Configuration Out of Code

This is unsafe:

```python
import anthropic

client = anthropic.Anthropic(api_key="sk-ant-the-real-secret")
```

The key now travels wherever the file travels. Deleting it later does not remove it from
old Git commits, saved notebook outputs, messages, or copies on other machines.

A `.env` file holds environment-variable assignments outside your program:

```text
ANTHROPIC_API_KEY=<secret value>
```

Your code asks for the value by name at runtime. The code can be shared; the `.env` cannot.

{: .note }
> A Python **virtual environment** is a directory containing an isolated interpreter and
> packages. An **environment variable** is a named runtime setting. A `.env` file is a
> convenient way to load environment variables. The similar names describe different
> things.

## Step 2: Confirm the Shared File Safely

The instructor has staged the course credential on the Yens. Print only the names of
variables it defines:

```bash
awk -F= '/^[A-Za-z_][A-Za-z0-9_]*=/{print $1}' /scratch/shared/yens-onboarding-2026/.env
```

You should see:

```text
ANTHROPIC_API_KEY
```

{: .warning }
> Do **not** run `cat` on a credential file. Terminal output is easy to capture in a
> screenshot, scrollback buffer, recording, support message, or agent context. Seeing the
> secret adds no useful information; the variable name is enough.

## Step 3: Copy It to the Repository Root

```bash
cd ~/yens-onboarding-2026
cp /scratch/shared/yens-onboarding-2026/.env .env
test -s .env && echo ".env exists and is not empty"
```

The scripts run from the repository root, so `load_dotenv()` will find this file without
an absolute path. Use one project-level copy rather than duplicating a secret across
folders.

## Step 4: Prove Git Ignores It

The repository already contains the `.env` rule. Verify the protection instead of
appending a duplicate:

```bash
git check-ignore -v .env
```

The command should print the matching `.gitignore` rule. You can also check how Git sees
the file:

```bash
git status --short --ignored .env
```

`!! .env` means ignored.

{: .warning }
> **A committed key is a leaked key.** Removing the line in a later commit does not repair
> the leak because Git preserves history. Revoke the credential immediately, replace it,
> and ask the repository owner for help removing the exposed value from history.

{: .important }
> Stop here if `git check-ignore -v .env` prints nothing. Do not stage or commit until the
> ignore rule is fixed.

## Step 5: Load It Without Printing It

In a notebook located in `day1/`, use the **GSB AI 2026** kernel:

```python
import os
from dotenv import load_dotenv

load_dotenv("../.env")
print("ANTHROPIC_API_KEY loaded:", bool(os.getenv("ANTHROPIC_API_KEY")))
```

You want `True`. That answers whether the key loaded without saving any part of it in the
notebook.

Scripts launched from the repository root use:

```python
from dotenv import load_dotenv

load_dotenv()
```

`python-dotenv` adds the values to the current Python process's environment. It does not
rewrite your source file.

{: .warning }
> Never run `print(os.environ)`, `print(key)`, or a masking function that exposes even a
> key prefix in a notebook. Notebook outputs are stored inside the `.ipynb` file. If you
> printed a secret, clear all outputs, save the notebook, and notify the instructor so the
> key can be revoked.

## Step 6: Initialize the Anthropic Client

```python
import anthropic

client = anthropic.Anthropic()
```

No key or base URL appears in the constructor. By convention, Anthropic's client reads
`ANTHROPIC_API_KEY` from the environment and uses Anthropic's API endpoint. This is both
safer and simpler than passing the secret through your code.

Confirm that the object exists without making a paid request:

```python
print(type(client).__name__)
```

The next section makes the first authenticated API call.

### Common Errors

| Symptom | Likely cause | Check |
|---|---|---|
| `ANTHROPIC_API_KEY loaded: False` | Wrong `.env` path | Run `pwd`; notebooks in `day1/` need `../.env` |
| Authentication error / HTTP `401` | Missing, mistyped, or revoked key | Re-copy the instructor file; do not print either copy |
| `.env` appears in `git status` | Ignore rule missing or file was already tracked | Stop and ask an instructor before committing |
| HTTP `429` | Request or token rate limit | Read the error and `retry-after`; do not keep rerunning immediately |

## If a Key Leaks

1. Stop using it and tell the key owner or instructor immediately.
2. Revoke and replace it. Treat this as the actual fix.
3. Clear notebook and terminal artifacts you control.
4. Remove the value from Git history with the repository owner's help.
5. Review logs and usage for unexpected calls.

Do not search GitHub for live secrets as an exercise. Finding a credential does not give
you permission to inspect or use it.

## Class Brainstorm: What Else Belongs in `.env`?

- API keys and access tokens
- database connection credentials
- cloud credentials
- machine-specific paths or service endpoints
- environment-specific settings such as an output directory

Secrets always belong outside source. Non-secret settings may also live in environment
variables when they differ between a laptop, the Yens, and a production job.

---

## Skills Learned

- Keep `ANTHROPIC_API_KEY` in `.env`, not in code or notebook output
- Verify a credential by name and presence without displaying its value
- Use `git check-ignore` to prove `.env` is excluded before committing
- Let `anthropic.Anthropic()` use the SDK's standard environment convention
- Revoke and replace a credential immediately if it leaks

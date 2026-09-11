# Yens Onboarding 2026

> **Stanford GSB DARC · Research computing & AI for incoming PhD students and faculty · 2 days · Hands-on**

A two-day, hands-on onboarding to research computing at Stanford GSB: the Yens cluster,
Git, Python environments, Stanford's AI API Gateway, Slurm batch jobs, and AI coding
tools. Both mornings run 9:00–12:00.

**🌐 Course website:** <https://gsbdarc.github.io/yens-onboarding-2026/>

There is no LMS this cohort — everything, including the optional extension material, is
on the course website.

---

## What You'll Learn

| Day | Focus | Topics, in order |
|-----|-------|------------------|
| **Day 1** | Foundations & AI | SSH & the Yens file system · Git & GitHub · Claude Code · Python on the Yens · virtual environments · Stanford's AI Gateway · AI agents & data privacy · API keys · LLM extraction with Pydantic validation |
| **Day 2** | The cluster | resource profiling · documenting what a job needs · writing & submitting `#SBATCH` jobs · reading logs & debugging failures · job arrays · rerun-safe tasks · array limits at scale · GPUs & local LLMs |

Both days build one pipeline over the same dataset — SEC Form 3 filings — turning
unstructured text into validated structured records, then scaling it across the cluster.

## Running the Site Locally

```bash
cd docs
bundle install
bundle exec jekyll serve --livereload
```

Then open <http://127.0.0.1:4000/yens-onboarding-2026/> — the `baseurl` in
`_config.yml` is why the path prefix is there.

`--livereload` does two things: Jekyll rebuilds the affected page when you save a
file, and the browser tab refreshes itself. Without the flag you still get the
rebuild, but you have to reload by hand. It serves LiveReload on port 35729
alongside the site on 4000.

One thing it does *not* pick up: `_config.yml` is read once at startup, so
restart the server after editing it.

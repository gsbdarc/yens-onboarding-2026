# Yens Onboarding 2026

> **Stanford GSB DARC · Research computing & AI for incoming PhD students and faculty · 2 days · Hands-on**

A two-day, hands-on onboarding to research computing at Stanford GSB: the Yens cluster,
Git, Python environments, Stanford's AI API Gateway, Slurm batch jobs, and AI coding
tools. Both mornings run 9:00–12:00.

**🌐 Course website:** <https://gsbdarc.github.io/yens-onboarding-2026/>

Pre-assignments, quizzes, and optional extension assignments are on **Canvas**.

---

## What You'll Learn

| Day | Focus | Skills |
|-----|-------|--------|
| **Day 1** | Foundations & AI | SSH · Yens file system · Git & GitHub · Claude Code · Python environments · Stanford AI Gateway · API keys · Pydantic validation |
| **Day 2** | The cluster | Resource profiling · Slurm · job lifecycle & logs · debugging failed jobs · Claude skills · job arrays · resource estimation |

Both days build one pipeline over the same dataset — SEC Form 3 filings — turning
unstructured text into validated structured records, then scaling it across the cluster.

## Repository Layout

```
docs/           the course website (Jekyll + just-the-docs, published by GitHub Actions)
  day1/         Day 1 sections
  day2/         Day 2 sections
  reference/    pre-work, plus material cut from class for time
  agenda.md     instructor run-of-show for both days
data/           SEC filings, the filing URL list, and the Potion Brawl demo project
scripts/        staged teaching scripts (extraction, profiling)
slurm/          example and deliberately-broken Slurm scripts
.instructor/    instructor-only: setup, Canvas spec, answer keys (not published)
```

## Running the Site Locally

```bash
cd docs
bundle install
bundle exec jekyll serve
```

## Prior Version

Condensed from the four-day
[gsbdarc/gsb-research-computing-ai-skills](https://github.com/gsbdarc/gsb-research-computing-ai-skills).
See [`docs/agenda.md`](docs/agenda.md) for what was cut and where it went.

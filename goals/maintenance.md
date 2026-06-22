# Maintenance

> **Goal-specific file.** Only relevant when
> `active_goal: maintenance` in [state.md](../state.md).

No active learning goal. The aim is to prevent existing knowledge
from going stale without committing to a study schedule.

---

## When to Use This Goal

- No interview planned and no domain to sprint
- You've completed a campaign or sprint and need a break
- You want a minimal cadence — one session every few days
- You are between goals

---

## How the System Adapts

Only Stale and Critical topics surface. Fresh and Medium topics
are skipped — they don't need attention yet.

**Filtered priority queue:**
- Include: Freshness = Stale (> 30 days) or Critical (> 60 days)
- Skip: Freshness = Fresh or Medium
- Skip: Mastery = 0 (not yet studied — belongs to Long-Term Mastery)

The goal is not to learn new material. It is to prevent regression
on topics you already know.

---

## Cadence

One session per week is usually enough.

1. Open [matrix/review_queue.md](../matrix/review_queue.md)
2. Filter for Stale or Critical only
3. Take the top topic — quick review only (10–15 min)
4. Update Freshness to Fresh and Last Reviewed date
5. Stop — do not do a full drill unless something felt shaky

If a topic feels shaky during a maintenance review, log it in
[hall_of_pain.md](../hall_of_pain.md) and note it needs a real
session. Do not try to fix it in a maintenance pass.

---

## Switching Goals

If an interview is scheduled: switch to `interview_campaign` or
`single_interview_prep`. Maintenance scores transfer directly.

If you want to learn new material: switch to `long_term_mastery`
or `domain_sprint`.

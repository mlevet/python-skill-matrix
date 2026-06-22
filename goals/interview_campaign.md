# Interview Campaign

> **Goal-specific file.** Only relevant when
> `active_goal: interview_campaign` in [state.md](../state.md).

A campaign covers a job-search period that may include multiple
technical interviews over weeks or months. Track the campaign here,
not individual interview dates in `state.md`.

---

## Campaign Status

| Field | Value |
|---|---|
| Status | Planning |
| First Expected Technical Interview | 2026-07-07 |
| Interview Window | July 2026 |
| Target Role | — |
| Target Seniority | — |

---

## Known Interviews

| Date | Company | Type | Status | Log |
|---|---|---|---|---|
| — | — | — | — | — |

*Add rows as interviews are confirmed. Link the Log column to an
entry in `interview_log/` after each interview.*

---

## Campaign Risks

*Fill in after baseline assessment. List the topics most likely to
hurt you given your skill profile and target role.*

→ See [matrix/interview_mode.md](../matrix/interview_mode.md) for
pre-computed risks based on current scores.

| Risk | Topic | Current Mastery | Freq | Score |
|---|---|---|---|---|
| 1 | Generators & `yield` | 0/10 | Very High | 40 |
| 2 | Late binding | 0/10 | Very High | 40 |
| 3 | Comprehensions | 0/10 | High | 30 |
| 4 | Context managers | 0/10 | High | 30 |
| 5 | LEGB scoping | 0/10 | High | 30 |

*Recalibrate after baseline assessment.*

---

## Campaign Strategy

*Fill in after baseline assessment and goal selection.*

**Time to first interview:** ~15 days
**Available sessions:** ~15 (1 per day)
**Session length:** 25–40 minutes

Recommended allocation:
- Days 1–10: Top 10 topics from [interview_mode.md](../matrix/interview_mode.md)
- Days 11–13: Hall of Pain review + code reading pass
- Days 14–15: Mock sessions — answer each top topic aloud, no notes

→ Full plan: [matrix/interview_mode.md](../matrix/interview_mode.md)

---

## After Each Interview

1. Add a row to the Known Interviews table above
2. Create an entry in `interview_log/`
3. Add any new surprises to [hall_of_pain.md](../hall_of_pain.md)
4. Update mastery scores in [matrix/skill_matrix.md](../matrix/skill_matrix.md)
5. Recalibrate [matrix/interview_mode.md](../matrix/interview_mode.md)
   if the next interview is more than a week away

---

## Closing the Campaign

When the campaign is over (offer received, search paused, or
decision to stop):

1. Set `interview_campaign.status: completed` in [state.md](../state.md)
2. Set `active_goal: not_selected` or `maintenance`
3. Log final lessons in `interview_log/`

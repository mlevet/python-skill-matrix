# Day 0 Readiness Audit

This is a self-assessment, not a study session.

**Time:** 60–90 minutes
**Goal:** Find out where you stand. Not to learn new material.

Take this once before you start studying. The output is your personal
review queue. Run it again after 4–6 weeks to measure progress.

---

## Why This Exists

Without a baseline, you are guessing what to study. You might spend
three sessions on a topic you already know, and miss a critical gap
that will surface in the first interview question.

This assessment exists to:

- identify what you actually know vs. what you think you know,
- identify the gaps most likely to hurt you in an interview,
- calibrate the skill matrix so the review queue is honest,
- generate realistic priorities instead of assumed ones.

**The goal is not learning. The goal is measurement.**

Study sessions come after. This comes first.

---

## Scoring scale

| Score | Meaning |
|---|---|
| 0 | Unknown — never heard of it |
| 1 | Recognized — I've seen this but can't explain it |
| 2 | Basic understanding — I get the idea |
| 3 | Interview-ready — I can explain it clearly |
| 4 | Can solve code-reading questions reliably |
| 5 | Can teach it confidently |

For each topic: rate yourself first, then answer the interview
question aloud (30 seconds), then predict the code output. Be honest.
"I thought I knew this" counts as a miss.

---

## Assessment files

Work through these in order. Each takes 10–20 minutes.

1. [Functional Python](functional_python.md) — 8 topics
2. [Iteration](iteration.md) — 6 topics
3. [OOP Internals](oop_internals.md) — 8 topics
4. [Runtime Behavior](runtime.md) — 7 topics
5. [Advanced Syntax](advanced_syntax.md) — 6 topics

---

## After the audit

1. Fill in [summary_template.md](summary_template.md)
2. Transfer scores to [matrix/skill_matrix.md](../matrix/skill_matrix.md)
3. Rebuild [matrix/review_queue.md](../matrix/review_queue.md) from
   your Weak and Medium results
4. Add any blanks or surprises to [hall_of_pain.md](../hall_of_pain.md)
5. Update [state.md](../state.md): set `baseline_assessment_completed: true`
   and `phase: goal_selection`

Then go to Step 6 — Goal Selection.

---

## Goal Selection

The assessment told you what you know. Now choose what you are
optimising for. These are two separate questions.

**Which goal fits your situation right now?**

### 1. Interview Campaign
You are in active job search. You expect multiple technical interviews
over the coming weeks or months.

Set in [state.md](../state.md):
```yaml
active_goal: interview_campaign
interview_campaign:
  status: planning
  first_expected_technical_interview: <date or "unknown">
  interview_window: <e.g. "July–August 2026">
  target_role: <e.g. "Backend Engineer">
  target_seniority: <e.g. "Senior">
```
→ Then open [goals/interview_campaign.md](../goals/interview_campaign.md)

---

### 2. Single Interview Preparation
You have one specific upcoming interview and are not in active search.

Set in [state.md](../state.md):
```yaml
active_goal: single_interview_prep
interview_campaign:
  status: planning
  first_expected_technical_interview: <date>
  target_role: <role>
  target_seniority: <level>
```
→ Then open [matrix/interview_mode.md](../matrix/interview_mode.md)

---

### 3. Long-Term Mastery
No deadline. You want to deepen Python broadly across all domains.

Set in [state.md](../state.md):
```yaml
active_goal: long_term_mastery
```
→ Then open [goals/long_term_mastery.md](../goals/long_term_mastery.md)

---

### 4. Domain Sprint
You want to complete one specific domain before moving on.

Set in [state.md](../state.md):
```yaml
active_goal: domain_sprint
domain_sprint:
  domain: <functional_python | oop | python_internals | advanced_syntax | ...>
```
→ Then open the relevant [roadmap](../roadmaps/)

---

### 5. Maintenance
No active goal. You just want to keep existing knowledge fresh.

Set in [state.md](../state.md):
```yaml
active_goal: maintenance
```
→ Then open [goals/maintenance.md](../goals/maintenance.md)

---

After updating [state.md](../state.md), open [dashboard.md](../dashboard.md).
The dashboard will now show goal-specific recommendations.

---

## What a good result looks like

You should end with a clear list of:
- 3–5 strong topics (mastery ≥ 4)
- 5–8 medium topics (mastery 2–3)
- The rest: weak or unknown

If everything feels weak, that is a useful result too. It means you
have a clear starting point.

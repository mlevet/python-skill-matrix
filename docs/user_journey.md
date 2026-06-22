# User Journey

How the system works from first use to long-term maintenance.
This document is for understanding the system, not for daily use.

---

```
New User
  │
  ▼
START_HERE.md
  │  Understand the three phases.
  │  Identify which phase you are in.
  │
  ▼
─────────────────────────────────────
PHASE 0 — CALIBRATION
─────────────────────────────────────
  │
  ▼
baseline_assessment/README.md
  │  35 topics · 60–90 minutes
  │  Self-rating + interview question + code reading per topic
  │
  ▼
baseline_assessment/summary_template.md
  │  Fill in Strong / Medium / Weak per domain
  │
  ▼
matrix/skill_matrix.md
  │  Transfer assessment scores (0–5 → 0–10 scale)
  │
  ▼
matrix/review_queue.md
  │  Rebuild from Weak and Medium results
  │
  ▼
state.md  →  phase: interview_preparation  (or maintenance)
  │
  ▼
─────────────────────────────────────
PHASE 1 — INTERVIEW PREPARATION
─────────────────────────────────────
  │
  ▼
dashboard.md  (every session)
  │  Check interview countdown and top priorities
  │
  ▼
matrix/interview_mode.md
  │  Top 10 topics · Top 5 high-risk gaps · study plan
  │
  ▼
Daily Session Loop  (25–40 min each)
  │
  ├── Topic file  →  read 30-second explanation
  ├── Drill file  →  solve exercises
  ├── Code reading  →  predict output, reveal answer
  ├── skill_matrix.md  →  update mastery + freshness
  └── hall_of_pain.md  →  log any surprises or blanks
  │
  ▼
Interview
  │
  ▼
─────────────────────────────────────
POST-INTERVIEW
─────────────────────────────────────
  │
  ▼
interview_log/
  │  Capture: unexpected topics, questions asked, gaps exposed
  │
  ▼
hall_of_pain.md
  │  Add any new entries from the interview
  │
  ▼
matrix/skill_matrix.md
  │  Update mastery scores based on how topics actually felt
  │
  ▼
state.md  →  phase: maintenance  (or interview_preparation if next date set)
  │
  ▼
─────────────────────────────────────
PHASE 2 — MAINTENANCE
─────────────────────────────────────
  │
  ▼
matrix/review_queue.md  (every few days)
  │  Review stale topics · deepen weak ones · add new domains
  │
  └── When new interview date confirmed:
      Update state.md  →  phase: interview_preparation
      Recalibrate matrix/interview_mode.md
```

---

## Key Invariants

- **state.md is always current.** It is the authoritative answer to
  "what phase am I in and what should I do next."
- **hall_of_pain.md grows over time.** Every surprise is an entry.
  Review it before every real interview.
- **skill_matrix.md drives everything.** The review queue, interview
  mode scores, and today's session all derive from it. Keep it honest.
- **The baseline assessment is a one-time calibration.** Re-run it
  after 6–8 weeks to measure progress, not sooner.

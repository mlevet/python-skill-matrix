# User Journey

How the system works from first use to long-term maintenance.
This document is for understanding the system, not for daily use.

---

```
New User
  │
  ▼
START_HERE.md
  │  Understand the phases.
  │  Identify where you are.
  │
  ▼
──────────────────────────────────────────
PHASE 0 — CALIBRATION
"What do I know?"
──────────────────────────────────────────
  │
  ▼
baseline_assessment/README.md
  │  35 topics · 60–90 minutes
  │  Self-rating + interview Q + code reading per topic
  │  Goal-agnostic: the same assessment regardless of why you're here.
  │
  ▼
baseline_assessment/summary_template.md
  │  Fill in Strong / Medium / Weak per domain
  │
  ▼
matrix/skill_matrix.md
  │  Transfer assessment scores
  │
  ▼
state.md  →  phase: goal_selection
  │
  ▼
──────────────────────────────────────────
PHASE 1 — GOAL SELECTION
"What am I trying to achieve?"
──────────────────────────────────────────
  │
  ├──── Technical Interview
  │       Set date, target_role, target_seniority in state.md
  │       │
  │       ▼
  │     matrix/interview_mode.md
  │       Top 10 topics · Top 5 high-risk gaps
  │       Scored by: freq_weight × (10 − mastery)
  │       │
  │       ▼
  │     Daily Sessions  →  dashboard.md each time
  │       Topic → Drill → Code Reading → Update skill_matrix
  │       │
  │       ▼
  │     Interview
  │       │
  │       ▼
  │     interview_log/  +  hall_of_pain.md
  │       │
  │       └──── back to Goal Selection
  │
  ├──── Long-Term Mastery
  │       No deadline. Broad coverage across all domains.
  │       │
  │       ▼
  │     matrix/review_queue.md  (every session)
  │       Follow priority order · update mastery · repeat
  │
  ├──── Domain Mastery
  │       Focus on one domain end-to-end.
  │       │
  │       ▼
  │     roadmaps/<domain>_path.md
  │       Follow steps · complete drills · code reading
  │       │
  │       └──── when path complete: back to Goal Selection
  │
  └──── Maintenance
          Keep existing knowledge fresh. Light cadence.
          │
          ▼
        matrix/review_queue.md  (every few days)
          Filter for Stale / Critical only
```

---

## Key Invariants

- **Calibration is goal-agnostic.** The baseline assessment is the
  same regardless of why you are here. It answers "what do I know?"
  Goal selection answers "what am I trying to achieve?" — a separate
  question answered after calibration.

- **state.md is always current.** Phase, goal, and next action are
  always up to date. When in doubt, open state.md.

- **skill_matrix.md drives everything.** Review queue, interview mode
  scores, and session recommendations all derive from it. Keep it honest.

- **hall_of_pain.md grows over time.** Every blank, surprise, and
  failed prediction is an entry. Review it before every real interview.

- **Re-run the baseline assessment after 6–8 weeks**, not sooner.
  It measures progress, not daily learning.

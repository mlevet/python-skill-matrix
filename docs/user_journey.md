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
──────────────────────────────────────────────────
PHASE 0 — CALIBRATION
"What do I know?"
Goal-agnostic. The same for every user.
──────────────────────────────────────────────────
  │
  ▼
baseline_assessment/README.md
  │  35 topics · 60–90 minutes
  │  Self-rating + interview Q + code reading per topic
  │
  ▼
baseline_assessment/summary_template.md
  │  Classify each domain: Strong / Medium / Weak
  │
  ▼
matrix/skill_matrix.md
  │  Transfer scores · rebuild review_queue.md
  │
  ▼
state.md  →  phase: goal_selection
  │
  ▼
──────────────────────────────────────────────────
PHASE 1 — GOAL SELECTION
"What am I trying to achieve?"
A separate question from calibration.
──────────────────────────────────────────────────
  │
  ▼
goals/README.md
  │  Choose one goal. Set active_goal in state.md.
  │
  ├──────────────────────────────────────────────
  │  INTERVIEW CAMPAIGN
  │  Active job search · multiple interviews expected
  │  ─────────────────────────────────────────────
  │  goals/interview_campaign.md
  │    Set: status, first_expected_interview, window,
  │         target_role, target_seniority
  │    │
  │    ▼
  │  matrix/interview_mode.md
  │    Top 10 topics · Top 5 risks
  │    Scored by: freq_weight × (10 − mastery)
  │    │
  │    ▼
  │  Daily Sessions  →  dashboard.md each time
  │    Topic → Drill → Code Reading → Update skill_matrix
  │    │
  │    ▼
  │  Interview  →  interview_log/  +  hall_of_pain.md
  │    │
  │    ▼
  │  Recalibrate interview_mode.md for next interview
  │    │
  │    └── Campaign complete → Goal Selection
  │
  ├──────────────────────────────────────────────
  │  SINGLE INTERVIEW PREPARATION
  │  One specific date · not in active job search
  │  ─────────────────────────────────────────────
  │  matrix/interview_mode.md  (same flow, one event)
  │    │
  │    └── After interview → Goal Selection
  │
  ├──────────────────────────────────────────────
  │  LONG-TERM MASTERY
  │  No deadline · broad coverage across all domains
  │  ─────────────────────────────────────────────
  │  goals/long_term_mastery.md
  │    │
  │    ▼
  │  matrix/review_queue.md  (every session)
  │    Follow priority order · no urgency tier
  │    │
  │    └── Interview scheduled → switch to campaign/prep
  │
  ├──────────────────────────────────────────────
  │  DOMAIN SPRINT
  │  One domain · end-to-end · then done
  │  ─────────────────────────────────────────────
  │  roadmaps/<domain>_path.md
  │    Follow steps · finish drills + code reading
  │    │
  │    └── Sprint complete → Goal Selection
  │
  └──────────────────────────────────────────────
     MAINTENANCE
     No active goal · prevent knowledge regression
     ─────────────────────────────────────────────
     goals/maintenance.md
       │
       ▼
     matrix/review_queue.md  (filtered: Stale/Critical only)
     One session per week
       │
       └── Goal changes → Goal Selection
```

---

## Key Invariants

- **Calibration is goal-agnostic.** "What do I know?" is answered
  once, independently of why you are here. Goal selection answers
  "what am I optimising for?" — a separate question, answered after.

- **state.md is always current.** Phase, goal, and next action are
  always up to date. When in doubt, open state.md.

- **Interview campaign ≠ global state.** The interview date lives
  inside `interview_campaign:` in state.md, not at the top level.
  A user doing Long-Term Mastery never sees or touches those fields.

- **skill_matrix.md drives everything.** Review queue, interview mode
  scores, and campaign risks all derive from it. Keep it honest.

- **hall_of_pain.md grows over time.** Every blank, surprise, and
  failed prediction is an entry. Review it before every real interview.

- **Re-run the baseline assessment after 6–8 weeks**, not sooner.
  It measures progress, not daily learning.

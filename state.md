# Repository State

> Update this file at each phase transition.
> It is the single source of truth for where you are and what to do next.

---

```yaml
# ── CALIBRATION ──────────────────────────────────────────────────────
baseline_assessment_completed: false
# Set to true after completing baseline_assessment/README.md

# ── GOAL ─────────────────────────────────────────────────────────────
goal: null
# Set this after completing the baseline assessment.
# Options:
#   technical_interview  — preparing for a specific interview
#   long_term_mastery    — deepen Python broadly, no deadline
#   domain_mastery       — focus on one specific domain
#   maintenance          — keep existing knowledge fresh

# ── GOAL-SPECIFIC CONFIG ─────────────────────────────────────────────
# Fill in only when goal: technical_interview
technical_interview:
  date: 2026-07-07
  target_role: null       # e.g. "Backend Engineer"
  target_seniority: null  # e.g. "Senior" / "Mid" / "Junior"

# Fill in only when goal: domain_mastery
domain_mastery:
  domain: null
  # Options: functional_python | oop | python_internals
  #          advanced_syntax | data_structures | concurrency

# ── PHASE (derived) ──────────────────────────────────────────────────
phase: calibration
# Derived from the fields above — do not set manually:
#   calibration     — assessment not completed
#   goal_selection  — assessment done, goal not yet set
#   active          — assessment done, goal set

# ── NEXT ACTION ──────────────────────────────────────────────────────
next_action: baseline_assessment/README.md
# Update after each transition:
#   calibration     → baseline_assessment/README.md
#   goal_selection  → START_HERE.md  (Goal Selection section)
#   active          → dashboard.md
```

---

## Phase Transitions

**Calibration → Goal Selection**
Trigger: baseline assessment completed.
1. Set `baseline_assessment_completed: true`
2. Transfer scores to `matrix/skill_matrix.md`
3. Set `phase: goal_selection`
4. Set `next_action: START_HERE.md`

**Goal Selection → Active**
Trigger: goal chosen.
1. Set `goal: <chosen_goal>`
2. Fill in the goal-specific config block if needed
3. Set `phase: active`
4. Set `next_action: dashboard.md`
5. Update phase banner in `dashboard.md` and `START_HERE.md`

**Active → Goal Selection** (after interview, after domain completed, etc.)
Trigger: goal achieved or changed.
1. Log results (interview_log/ or hall_of_pain.md)
2. Set `goal: null`
3. Set `phase: goal_selection`
4. Set `next_action: START_HERE.md`

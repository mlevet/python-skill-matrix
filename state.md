# Repository State

> Update this file at each phase transition.
> It is the single source of truth for where you are and what to do next.

---

```yaml
# ── CALIBRATION ──────────────────────────────────────────────────────
baseline_assessment_completed: false
# Set to true after completing baseline_assessment/README.md

# ── GOAL ─────────────────────────────────────────────────────────────
active_goal: not_selected
# Set this after completing the baseline assessment.
# Options:
#   not_selected             — goal not yet chosen
#   interview_campaign       — active job search with multiple interviews
#   single_interview_prep    — one specific upcoming interview
#   long_term_mastery        — broaden Python, no deadline
#   domain_sprint            — complete one domain end-to-end
#   maintenance              — keep existing knowledge fresh

# ── INTERVIEW CAMPAIGN (fill in when active_goal: interview_campaign) ─
interview_campaign:
  status: inactive
  # Options: inactive | planning | active | paused | completed
  first_expected_technical_interview: unknown
  interview_window: unknown
  target_role: null         # e.g. "Backend Engineer"
  target_seniority: null    # e.g. "Senior" / "Mid" / "Junior"
  known_interviews: []
  # Add entries as they are confirmed:
  # - date: 2026-07-07
  #   company: "Acme Corp"
  #   type: "Technical"
  #   status: "Scheduled"

# ── DOMAIN SPRINT (fill in when active_goal: domain_sprint) ──────────
domain_sprint:
  domain: null
  # Options: functional_python | oop | python_internals
  #          advanced_syntax | data_structures | concurrency

# ── PHASE (derived) ──────────────────────────────────────────────────
phase: calibration
# Derived from the fields above:
#   calibration     — baseline_assessment_completed: false
#   goal_selection  — assessment done, active_goal: not_selected
#   active          — assessment done, goal set

# ── NEXT ACTION ──────────────────────────────────────────────────────
next_action: baseline_assessment/README.md
# Update after each transition:
#   calibration     → baseline_assessment/README.md
#   goal_selection  → goals/README.md
#   active          → dashboard.md  (or goal-specific file)
```

---

## Phase Transitions

**Calibration → Goal Selection**
Trigger: baseline assessment completed.
1. Set `baseline_assessment_completed: true`
2. Transfer scores to `matrix/skill_matrix.md`
3. Set `phase: goal_selection`
4. Set `next_action: goals/README.md`

**Goal Selection → Active**
Trigger: goal chosen.
1. Set `active_goal: <chosen_goal>`
2. Fill in the goal-specific config block if applicable
3. Set `phase: active`
4. Set `next_action: dashboard.md`
5. Update phase banners in `dashboard.md` and `START_HERE.md`

**Active → Goal Selection**
Trigger: goal completed, interview passed, sprint finished, etc.
1. Log results (interview_log/ or hall_of_pain.md)
2. Set `active_goal: not_selected`
3. Clear the goal-specific config block
4. Set `phase: goal_selection`
5. Set `next_action: goals/README.md`

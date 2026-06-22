# Repository State

> Update this file whenever your phase changes or your interview date
> shifts. It is the single source of truth for where you are.

---

```yaml
phase: calibration
# Options:
#   calibration          — baseline assessment not yet completed
#   interview_preparation — assessment done, interview date set
#   maintenance          — no interview in next 4 weeks

baseline_assessment_completed: false
# Set to true after completing baseline_assessment/README.md

next_interview:
  date: 2026-07-07
  days_remaining: 15    # update daily

next_action: baseline_assessment/README.md
# What to open right now — update after each phase transition:
#   calibration          → baseline_assessment/README.md
#   interview_preparation → dashboard.md
#   maintenance          → matrix/review_queue.md
```

---

## Phase Transitions

**Calibration → Interview Preparation**
When to switch: baseline assessment completed and interview date set.
What to do:
1. Set `baseline_assessment_completed: true`
2. Set `phase: interview_preparation`
3. Set `next_action: dashboard.md`
4. Update `dashboard.md` phase banner

**Interview Preparation → Maintenance**
When to switch: interview passed, no new date set.
What to do:
1. Set `phase: maintenance`
2. Set `next_action: matrix/review_queue.md`
3. Update `dashboard.md` phase banner

**Maintenance → Interview Preparation**
When to switch: new interview date confirmed.
What to do:
1. Set `phase: interview_preparation`
2. Set `next_interview.date` and `days_remaining`
3. Set `next_action: dashboard.md`
4. Recalibrate `matrix/interview_mode.md`

# Goals

Choose a goal after completing the baseline assessment.

The goal tells the system what you are optimising for. It changes
what the dashboard shows, which topics get prioritised, and how
urgency is calculated.

Update `active_goal` in [state.md](../state.md) when you choose.

---

## Available Goals

### Interview Campaign
**Use when:** you are in active job search and expect multiple
technical interviews over a period of weeks or months.

Tracks a campaign with a window, a target role, and individual
interviews as events. Prioritises topics by frequency × weakness,
compressed by time to first expected interview.

→ [goals/interview_campaign.md](interview_campaign.md)

---

### Single Interview Preparation
**Use when:** you have one specific upcoming interview and are not
in active job search.

Simpler than a campaign — set one date, one role, and focus until
the interview. Transitions to Maintenance or a new goal after.

→ No separate file. Set `active_goal: single_interview_prep` and
fill in the `interview_campaign` block for that one interview.
→ [matrix/interview_mode.md](../matrix/interview_mode.md) for topic plan.

---

### Long-Term Mastery
**Use when:** no interview deadline. You want to deepen Python
across all domains and keep knowledge fresh over months.

Prioritises breadth and freshness. No countdown, no urgency tier.
Sessions are driven by the review queue and staleness.

→ [goals/long_term_mastery.md](long_term_mastery.md)

---

### Domain Sprint
**Use when:** you want to complete one specific domain end-to-end
before moving on.

Set the domain in `state.md`, follow the roadmap step by step,
finish all drills and code reading for that domain.

→ Set `domain_sprint.domain` in [state.md](../state.md), then open
the relevant [roadmap](../roadmaps/).

---

### Maintenance
**Use when:** no active goal — you just want to prevent existing
knowledge from going stale.

Light cadence. Only Critical and Stale topics surface. No new
domains, no pressure.

→ [goals/maintenance.md](maintenance.md)

---

## Choosing

If you are unsure, answer these questions:

1. Do you have an interview coming up in the next 8 weeks?
   → Yes: Interview Campaign or Single Interview Preparation
   → No: continue

2. Is there a specific domain you feel seriously weak in?
   → Yes: Domain Sprint
   → No: continue

3. Are you actively studying or just keeping things fresh?
   → Studying: Long-Term Mastery
   → Keeping fresh: Maintenance

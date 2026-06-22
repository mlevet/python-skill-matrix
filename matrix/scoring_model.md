# Scoring Model

---

## Confidence scale (0–5)

| Score | Meaning |
|---|---|
| 0 | Never studied — blank |
| 1 | Aware it exists, can't explain it |
| 2 | Rough idea, can explain concept but not code it live |
| 3 | Can explain AND write it with some effort or minor lookup |
| 4 | Fluent — explain + code correctly under mild pressure |
| 5 | Interview-ready — no hesitation, can handle follow-up questions |

**Target for interview:** every high-frequency topic at ≥ 4.  
**Realistic minimum:** every topic you list at ≥ 2 before an interview.

---

## Interview frequency

| Label | Meaning |
|---|---|
| high | Appears in most Python technical screens |
| medium | Appears in deeper Python or senior-level interviews |
| low | Niche — useful to know, unlikely to be asked directly |

---

## Priority score

Used to sort [matrix/review_queue.md](matrix/review_queue.md).

```
priority = freq_weight × (5 - confidence) × staleness_factor
```

Where:
- `freq_weight`: high=3, medium=2, low=1
- `(5 - confidence)`: gap to interview-ready
- `staleness_factor`: 1 + (days_since_review / 30)

Higher priority = review first.

You don't need to calculate this exactly — use it as a mental model:  
**High-freq + low-confidence + stale = top of queue.**

---

## How to update scores

After every review session:

1. Set `last_reviewed` to today's date (YYYY-MM-DD).
2. Adjust confidence based on how it went:

| What happened | Adjustment |
|---|---|
| Explained it correctly, first try | +0 or +1 |
| Explained but needed a prompt | +0 |
| Needed to look up syntax | -0 or -1 |
| Couldn't code it at all | -1 or -2 |
| Got a code-reading puzzle wrong on this topic | -1 |
| Nailed a hard puzzle on this topic | +1 |

3. Re-sort the review queue if your top priority changed.

---

## Anti-patterns to avoid

- **Phantom confidence:** giving yourself a 4 because you understand it now, right after reading the answer. Test yourself first.
- **Staleness blindness:** a topic you scored 5 six months ago is not still a 5 — freshness decays.
- **Queue avoidance:** the topic you keep skipping is always the one you need most.

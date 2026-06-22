# Scoring Model

---

## Mastery scale (0–10)

| Score | Meaning |
|---|---|
| 0 | Unknown — never studied |
| 3 | Recognized but weak — aware it exists, can't explain it |
| 5 | Understands basics — can explain the concept, struggles to code it live |
| 7 | Can explain in interview — fluent explanation, can write it under pressure |
| 10 | Can explain, code, debug, and teach — no hesitation, handles follow-ups |

**Interview target:** every High-frequency topic at ≥ 7.

---

## Interview Frequency weights

| Label | Weight | Meaning |
|---|---|---|
| Low | 1 | Niche — useful to know, rarely asked directly |
| Medium | 2 | Appears in deeper Python or senior-level interviews |
| High | 3 | Appears in most Python technical screens |
| Very High | 4 | Almost guaranteed — expect follow-up questions |

---

## Freshness weights

| Label | Weight | Meaning |
|---|---|---|
| Fresh | 1 | Reviewed in the last 7 days |
| Medium | 2 | Reviewed in the last 30 days |
| Stale | 3 | Not reviewed in 30+ days |
| Critical | 4 | Important topic not reviewed in 60+ days |

---

## Priority formula

```
Priority = Interview Frequency Weight × (10 − Mastery) × Freshness Weight
```

Higher priority = review first. The formula surfaces high-value stale topics before low-value fresh ones.

### Example — Closures

| Factor | Value | Weight |
|---|---|---|
| Interview Frequency | High | 3 |
| Mastery | 5/10 | — |
| Freshness | Stale | 3 |

```
Priority = 3 × (10 − 5) × 3 = 45
```

### Example — Import system

| Factor | Value | Weight |
|---|---|---|
| Interview Frequency | Low | 1 |
| Mastery | 0/10 | — |
| Freshness | Stale | 3 |

```
Priority = 1 × (10 − 0) × 3 = 30
```

Closures (45) ranks above Import system (30) even though Import system has lower mastery — because interview frequency dominates.

### Priority range

| Scenario | Priority |
|---|---|
| Very High freq, mastery 0, Critical freshness | 4 × 10 × 4 = **160** |
| High freq, mastery 0, Stale | 3 × 10 × 3 = **90** |
| High freq, mastery 7, Stale | 3 × 3 × 3 = **27** |
| Medium freq, mastery 5, Medium | 2 × 5 × 2 = **20** |
| Low freq, mastery 10, Fresh | 1 × 0 × 1 = **0** (mastered — skip) |

---

## How to update after a session

1. Set `Last Reviewed` to today's date (`YYYY-MM-DD`).
2. Adjust `Mastery` based on how the session went:

| What happened | Adjustment |
|---|---|
| Explained it correctly without notes, first try | +1 or +2 |
| Explained it but needed a prompt or hint | +0 |
| Needed to look up syntax or details | −1 |
| Couldn't explain or code it | −2 |
| Got a code-reading puzzle wrong on this topic | −1 |
| Nailed a hard puzzle cold | +1 |

3. Update `Freshness` based on the new `Last Reviewed` date.
4. Recompute `Priority` and re-sort [review_queue.md](review_queue.md) if the top changed.

---

## Anti-patterns to avoid

- **Phantom mastery:** giving yourself a 7 right after reading the answer. Test yourself before looking.
- **Staleness blindness:** a topic scored 8 six months ago is not still an 8. Freshness decays.
- **Queue avoidance:** the topic you keep skipping is the one you need most.
- **Over-optimising low-freq topics:** a Low-frequency topic at 0/10 scores 30 — lower than a High-frequency topic at 7/10 (score 27, but interview frequency makes it the priority). Don't spend session time on Low topics when High ones are stale.

# Daily Routine

A realistic 15–30 minute daily session. Adapt to how much time you have.

---

## The 4-step loop

### 1. Orient (2 min)
Open [dashboard.md](dashboard.md).  
Check the top item in the review queue.  
Decide: review a topic, run a drill, or do a code-reading puzzle?

**Rule:** never open the repo without deciding what you're doing in the first 2 minutes.

---

### 2. Review or drill (10–20 min)

**Option A — Topic review**
1. Open the topic file in `domains/`.
2. Read the summary and key concepts.
3. Cover the examples and try to reproduce them from memory.
4. Run the matching drill in `drills/` if one exists.
5. Update `confidence` and `last_reviewed` in [matrix/skill_matrix.md](matrix/skill_matrix.md).

**Option B — Code-reading drill**
1. Pick a puzzle from [code_reading/](code_reading/) (start easy if warming up).
2. Write your answer before reading the spoiler.
3. Check the trap/concept — add it to `traps_index.md` if it's new to you.
4. If you got it wrong, bump the related topic's confidence down by 1.

**Option C — New topic (only if queue is empty above)**
1. Copy `templates/topic_template.md` into the right domain folder.
2. Fill in as much as you know without looking things up first.
3. Then verify, fill gaps, add examples.
4. Set confidence honestly.

---

### 3. Update the matrix (2 min)

After every review:

- Set `last_reviewed` to today's date.
- Adjust `confidence` up or down based on how it felt.
- Re-sort [matrix/review_queue.md](matrix/review_queue.md) if the priority changed significantly.

**Confidence adjustment heuristics:**
- Explained it correctly, first try → keep or +1
- Needed to look something up → keep or -1
- Got a code-reading puzzle wrong → -1 on the related topic
- Couldn't code it at all → -2

---

### 4. Set tomorrow's target (1 min)

Write one line at the top of [dashboard.md](dashboard.md) for next session:

```
Next: review closures (confidence=2, 14 days stale)
```

---

## Weekly rhythm

| Day | Focus |
|---|---|
| Mon | Functional Python (lambdas, closures, decorators) |
| Tue | OOP internals (dunder, MRO, descriptors) |
| Wed | Code-reading — medium/hard puzzles |
| Thu | Python internals (scoping, GC, data model) |
| Fri | Weakest topic of the week (check review queue) |
| Sat | Mock interview drill — pick 5 topics, explain each in 2 min |
| Sun | Optional — update roadmap, log progress |

Adjust based on upcoming interview dates.

---

## When you have only 5 minutes

1. Open review queue.
2. Pick the top topic.
3. Read only the **Summary** and **Common traps** sections.
4. Do not update confidence unless you actually tested yourself.

---

## Signs the system is working

- You can explain any confidence-4 topic in under 2 minutes without notes.
- You recognize traps in code-reading puzzles before finishing the snippet.
- The review queue never goes stale — you have a "last reviewed" date on everything within the past 30 days.

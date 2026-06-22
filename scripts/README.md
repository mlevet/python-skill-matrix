# Scripts

Optional helper scripts for automating parts of the system.

None are required — the system works entirely with manual Markdown updates.

---

## Planned / potential scripts

### `score_summary.py`

Parse `matrix/skill_matrix.md`, compute average confidence per domain and overall, print a summary.

```
Usage: python scripts/score_summary.py
```

### `stale_topics.py`

Parse `skill_matrix.md`, find topics where `last_reviewed` is more than N days ago and confidence < 4, and print a sorted list.

```
Usage: python scripts/stale_topics.py [--days 14]
```

### `random_drill.py`

Pick a random topic from a given domain and open its topic file (or print the path).

```
Usage: python scripts/random_drill.py [--domain functional_python]
```

---

## When to add a script

Only add a script if a manual update is taking more than 2 minutes per session. The overhead of maintaining scripts that parse Markdown is not always worth it. Keep the system lean.

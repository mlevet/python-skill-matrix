# Today's Session — Lambda Functions

**Date:** 2026-06-22  
**Time:** ~30 minutes  
**Topic:** Lambda Functions (mastery 6/10, Medium freshness)  
**Goal:** Lock in the late-binding trap and the sort-key pattern.

---

## Step 1 — Quick review (5 min)

Glance at [Functions as Objects](domains/functional_python/functions_as_objects.md).
Read only the Mental model section. Close the file.

Say aloud: "A function is an object. Assigning it to a new variable
creates a second reference, not a copy."

---

## Step 2 — Read the topic (5 min)

→ [Lambda Functions](domains/functional_python/lambda_functions.md)

After reading: close the file. Explain what a lambda is, what it
cannot do, and what the late-binding trap is — in 30 seconds, aloud.

---

## Step 3 — Code reading (5 min)

Before opening the answer, write your prediction on paper.

→ [M1 — Classic late binding closure](code_reading/medium.md)

Predicted output: `_______`

---

## Step 4 — Drills (10 min)

Open [drills/lambdas.py](drills/lambdas.py). Work through these:

**Exercise 3 — Late binding trap**
Predict the output of `broken`, verify, then predict `fixed`.
This is the most commonly asked lambda question in interviews.

**Exercise 7 — Multi-key sort**
Predict `sorted(people, key=lambda p: (p[1], p[0]))`.
Sorting with a lambda key is a standard interview task.

**Exercise 8 — Lambda vs def**
Predict `square_lambda.__name__`. This is a subtle `__name__`
trap that appears in logging and debugging questions.

---

## Step 5 — Update (2 min)

In [matrix/skill_matrix.md](matrix/skill_matrix.md):

- Lambda Functions: set Freshness → Fresh, Last Reviewed → 2026-06-22
- Adjust Mastery: was 6/10. Did the late-binding trap feel solid?
  If yes → 7. If still uncertain → keep at 6.

If anything surprised you, add an entry to
[hall_of_pain.md](hall_of_pain.md).

---

## Next session

→ [Closures](domains/functional_python/closures.md)  
→ [Drill](drills/closures.py): Exercises 1, 2, 3  
→ [Code Reading H7](code_reading/hard.md)

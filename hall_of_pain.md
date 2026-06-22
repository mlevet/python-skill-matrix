# Hall of Pain

Every time you fail a drill, get surprised, blank during a mock, or miss a question in a real interview — it goes here. Review this file before every interview.

---

## 2026-06-22

**Topic:** Lambda late binding

**Mistake:** Assumed each lambda in a loop captured the current value of the loop variable at the time it was created.

**Reality:** Closures capture the variable name, not the value. By the time any of the lambdas is called, the loop has finished and the variable holds its final value. All lambdas see the same result.

**Action:** Study `closures.md` and `late_binding.md`. Added 3 code-reading puzzles on this exact trap (see M1 and E11 in `code_reading/`).

**Status:** Studying

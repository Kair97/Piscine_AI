# Progress Tracker
> Updated at the end of every session by Claude.

---

## Module: python_basics
**Repo:** https://01.tomorrow-school.ai/git/kaorynbek/python-basics
**Deadline:** 2026-06-16
**Notebook:** `Day01.ipynb`

### Exercises
- [ ] Exercise 0 — Environment setup *(in progress)*
- [ ] Exercise 1 — Variables and types
- [ ] Exercise 2 — Operators and expressions
- [ ] Exercise 3 — Strings
- [ ] Exercise 4 — Control flow
- [ ] Exercise 5 — Loops
- [ ] Exercise 6 — Functions
- [ ] Exercise 7 — Scope

---

## Session Log

### 2026-06-15 — Session 1
**What was done:**
- Discovered Kairo has Python 3.10, 3.12, 3.13, 3.14 installed on Windows
- Resolved PATH conflict — msys64 was overriding Python 3.14
- Solution: use `py -3.14 -m venv ex00` to create virtual environments
- Created `Piscine_AI/python_basics/` directory structure
- Created `CLAUDE.md` and initialized vault

**Next step:**
- Run `py -3.14 -m venv ex00` inside `python_basics/`
- Activate venv: `ex00\Scripts\activate`
- Run `pip install jupyter`
- Run `pip freeze > requirements.txt`
- Launch `jupyter notebook` and create `Day01.ipynb`
- Complete Exercise 0 verification cell (`import sys; print(sys.version)`)
- Then move to Exercise 1

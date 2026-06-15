# Errors Log
> This file is automatically maintained by Claude. Every error encountered during the Piscine is logged here. Claude reads this at the start of every session to avoid repeating mistakes.

---

## [2026-06-15] Error: Wrong Python version being used by default

**Context:** Exercise 0 — Setting up the environment
**Error message:** `python --version` returned `Python 3.12.7` instead of expected 3.14
**Root cause:** `msys64` Python installation was at the top of the system PATH, overriding all other Python versions including 3.14
**Fix:** Use `py -3.14 -m venv ex00` instead of `python -m venv ex00` to explicitly target Python 3.14 when creating virtual environments. Once inside the venv, `python` works correctly.
**Lesson:** On Kairo's machine, never use bare `python` command outside a venv. Always use `py -3.14` to create venvs. Check with `where python` if something seems wrong.

---

## [2026-06-15] Error: Wrong dialog opened in Environment Variables

**Context:** Trying to add Python 3.14 to PATH via Windows Environment Variables UI
**Error message:** N/A (UI mistake)
**Root cause:** Clicked "New" to create a new variable instead of selecting the existing "Path" variable and clicking "Edit". Also accidentally clicked on "CABAL_DIR" instead of "Path".
**Fix:** In Environment Variables → User variables → click on the row that says **Path** → then click **Edit** → then inside that window click **New** to add entries.
**Lesson:** The PATH variable already exists. Never create a new variable for path entries. Always edit the existing "Path" variable.

---

*New errors will be appended here as they occur.*

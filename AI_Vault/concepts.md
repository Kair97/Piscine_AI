# Python Concepts — Personal Reference
> This file grows every session. Each concept is explained in simple words based on Kairo's learning journey.

---

## Python Version Management (Windows)
**Learned during:** Exercise 0 — Setup
**In simple words:** Windows can have multiple Python versions installed at the same time. The `py` launcher lets you pick which one to use with `-3.XX`. Once you're inside a virtual environment, it always uses the right version automatically.

**Key commands:**
```bash
py -0                    # list all installed Python versions
py -3.14 --version       # check specific version
py -3.14 -m venv ex00   # create venv with specific version
where python             # see which python cmd uses by default
```

**Gotcha:** The `msys64` package manager installs its own Python and puts it first in PATH. This means `python` on Kairo's machine points to 3.12 (msys64), not 3.14. Always use `py -3.14` when creating venvs outside of an activated environment.

---

## Virtual Environments
**Learned during:** Exercise 0 — Setup
**In simple words:** A virtual environment is like a clean, isolated box for your project. It has its own Python and its own libraries, so projects don't interfere with each other.

**Key commands:**
```bash
py -3.14 -m venv ex00       # create
ex00\Scripts\activate        # activate (Windows)
pip install jupyter          # install packages inside venv
pip freeze > requirements.txt  # save list of installed packages
deactivate                   # exit the venv
```

**Gotcha:** Always activate the venv before installing packages or running Jupyter. You'll see `(ex00)` in your terminal when it's active.

---

*New concepts will be added here as exercises are completed.*

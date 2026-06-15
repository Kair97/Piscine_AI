# CLAUDE.md — Piscine AI @ Tomorrow School
> Instruction file for Claude Code. Read this file entirely before doing anything in this repository.

---

## 1. WHO YOU ARE AND WHAT THIS IS

You are an AI coding assistant helping **Kairo** complete the **AI Piscine at Tomorrow School (01.astanahub.com)**. This is a structured learning program where Kairo learns Python, data science, and ML from scratch — by writing all code himself. Your role is to **guide, explain, and review** — not to write solutions for him unless explicitly asked.

This repository lives at:
```
Piscine_AI/
├── python_basics/        ← Current active module
├── vault/                ← Obsidian knowledge vault (see Section 4)
└── CLAUDE.md             ← This file
```

---

## 2. YOUR CORE RESPONSIBILITIES

### Always do this at the start of every session:
1. Read `vault/errors.md` — know what mistakes have been made before, never repeat them
2. Read `vault/progress.md` — know exactly where Kairo left off
3. Read `vault/context.md` — understand current task, goals, and environment

### Always do this at the end of every session:
1. Update `vault/errors.md` with any new errors encountered and how they were fixed
2. Update `vault/progress.md` with what was completed
3. Update `vault/context.md` with current state so next session has full awareness

---

## 3. RULES FOR WORKING WITH KAIRO

- **Kairo writes the code himself.** Do not write full solutions unprompted. He is here to learn.
- When he is stuck, give hints and explanations first, not the answer.
- If he explicitly asks for the answer or full code, provide it — but always explain it line by line.
- Use simple, clear language. He is learning Python as a beginner.
- When he makes a mistake, explain **why** it is wrong, not just what the fix is.
- Always point to the relevant exercise number when giving feedback.
- Celebrate progress. Learning is hard.

---

## 4. THE VAULT — KNOWLEDGE BASE

The vault is an Obsidian markdown folder at `vault/`. It is your persistent memory across sessions. Treat it as a living document — read it, update it, improve it every session.

### vault/errors.md
A log of every error encountered. Format:

```markdown
## [DATE] Error: <short title>
**Context:** Which exercise / what were we doing
**Error message:** (exact error if applicable)
**Root cause:** Why it happened
**Fix:** What solved it
**Lesson:** What to remember to avoid this next time
---
```

### vault/progress.md
Tracks exactly what has been done. Format:

```markdown
## Module: python_basics
- [x] Exercise 0 — Environment setup (completed: 2026-06-15)
- [ ] Exercise 1 — Variables and types
- [ ] Exercise 2 — Operators and expressions
- [ ] Exercise 3 — Strings
- [ ] Exercise 4 — Control flow
- [ ] Exercise 5 — Loops
- [ ] Exercise 6 — Functions
- [ ] Exercise 7 — Scope

**Last session:** <date and what was done>
**Next step:** <exactly what to do next>
```

### vault/context.md
A snapshot of the current state. Format:

```markdown
## Current Environment
- Python version: 3.14
- Virtual env: ex00 (located in python_basics/)
- Notebook: Day01.ipynb

## Current Task
Module: python_basics
Exercise: <current exercise number and name>
Status: <in progress / blocked / done>

## What Kairo understands well
- <topics>

## What Kairo struggles with
- <topics>

## Open questions / blockers
- <any unresolved issues>
```

### vault/concepts.md
Key Python concepts explained in Kairo's own learning journey. Add a new entry whenever a new concept is learned or clarified. This grows into a personal Python reference. Format:

```markdown
## <Concept Name>
**Learned during:** Exercise X
**In simple words:** <plain English explanation>
**Example:**
```python
# code example
```
**Gotcha / common mistake:** <what to watch out for>
---
```

---

## 5. ENVIRONMENT

| Setting | Value |
|---|---|
| OS | Windows 11 |
| Python | 3.14 (via `py -3.14`) |
| Virtual env tool | venv |
| Notebook | Jupyter (`Day01.ipynb`) |
| Working dir | `Piscine_AI/python_basics/` |
| Repo | https://01.tomorrow-school.ai/git/kaorynbek/python-basics |

### Activating the environment (Windows):
```bash
cd Piscine_AI/python_basics
ex00\Scripts\activate
jupyter notebook
```

### Known PATH issue:
`msys64` Python overrides the default `python` command. Always use `py -3.14` to create venvs. Once inside a venv, `python` works correctly.

---

## 6. CURRENT MODULE — PYTHON BASICS

### Module goal:
Understand core Python syntax and semantics before moving to NumPy, Pandas, and ML libraries.

### Submission:
- Git repo: `https://01.tomorrow-school.ai/git/kaorynbek/python-basics`
- All work done in `Day01.ipynb`
- `requirements.txt` must be present

### Timeline:
- Start: 2026-06-15
- End: 2026-06-16

---

## 7. ORIGINAL TASK REQUIREMENTS (VERBATIM)

> The following is the **exact, unmodified** task description from Tomorrow School's intra platform.

---

### Overview

The goal of this day is to understand the core syntax and semantics of Python. Python is a dynamically typed, interpreted language that data scientists and ML engineers use for everything from data wrangling to deploying models in production. Before working with NumPy, Pandas, or any ML library, you need to be fluent in the language itself. This day covers the building blocks: variables, built-in data types, operators, control flow, functions, and scope. Every exercise that follows in this Piscine will rely on these constructs, and fluency here removes the friction from all subsequent work. Learners who have written Go or JavaScript will find Python's syntax familiar in structure but different in semantics — particularly around dynamic typing, mutability, and first-class functions.

---

### Role Play

You are a junior data analyst joining a logistics company. Your first week requires you to audit and prototype small Python scripts that process delivery records. Before your team lead grants you access to the company's data pipeline, she has asked you to demonstrate competence with Python fundamentals by passing an internal code review.

---

### Learning Objectives

- Declare variables and identify the type returned by `type()` for Python's built-in types.
- Apply arithmetic, comparison, and logical operators to produce correct results, including short-circuit evaluation.
- Format strings using f-strings and manipulate them with built-in string methods.
- Construct conditional logic with `if`, `elif`, and `else` branches.
- Iterate over sequences and ranges using `for` and `while`, and control flow with `break` and `continue`.
- Define functions with positional arguments, default values, `*args`, `**kwargs`, and explicit return statements.
- Reason about variable scope using the LEGB (Local, Enclosing, Global, Built-in) rule.

---

### Exercise 0: Environment and libraries

The goal of this exercise is to set up the Python work environment with the required libraries and to learn to launch a Jupyter notebook.

Create a virtual environment named `ex00` using Python >= 3.10. Install `jupyter`. Save the installed packages to a file named `requirements.txt` in the current directory. Launch a Jupyter notebook or JupyterLab. Create a new notebook named `Day01`.

In the first cell, verify your Python version:
```python
import sys
print(sys.version)
```

---

### Exercise 1: Variables and types

1. Create one variable of each of the following types: `int`, `float`, `str`, `bool`, `NoneType`. Print each variable and the result of `type()` on it, one per line.

Expected output:
```
42 <class 'int'>
3.14 <class 'float'>
hello <class 'str'>
True <class 'bool'>
None <class 'NoneType'>
```

2. Without declaring new variables, use the five variables from step 1 to check:
- Is `int` a subclass of `bool`? (use `issubclass`)
- Is `bool` a subclass of `int`?
- Does `type(True) == type(1)` evaluate to `True`?

Expected output:
```
False
True
False
```

3. Create `a = [1, 2, 3]` and `b = a`. Append 4 to `b`. Print both `a` and `b`, then print the result of `a is b`.

Expected output:
```
[1, 2, 3, 4]
[1, 2, 3, 4]
True
```

---

### Exercise 2: Operators and expressions

1. Given `x = 17` and `y = 5`, compute and print: integer division, modulo, exponentiation, and true division.

Expected output:
```
integer division: 3
modulo: 2
exponentiation: 1419857
true division: 3.4
```

2. Short-circuit evaluation:
```python
print(0 or "default")
print("found" or "default")
print(None and "unreachable")
print("left" and "right")
```

Expected output:
```
default
found
None
right
```

3. Operator precedence:
```python
print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 ** 2)
print(not True or False)
print(not (True or False))
```

---

### Exercise 3: Strings

1. Given `name = "Alice"` and `score = 98.6`, produce using an f-string:
```
Student: Alice | Score: 98.60
```

2. Given `sentence = "  the quick brown fox  "`, produce using one method call per line:
```
THE QUICK BROWN FOX
the quick brown fox
The Quick Brown Fox
the quick brown fox
```

3. Given `csv_line = "Paris,France,2161000"`, split and print each field prefixed by index:
```
0: Paris
1: France
2: 2161000
```

4. Count how many times `"ai"` appears in `"artificial intelligence trains on data daily"` using case-insensitive search. Expected output: `2`

---

### Exercise 4: Control flow

1. Write `classify_bmi(bmi)` that returns: `"Underweight"` / `"Normal"` / `"Overweight"` / `"Obese"` based on BMI ranges. Test with 16.0, 22.4, 27.1, 35.8.

2. Write `fizzbuzz(n)` that returns `"FizzBuzz"`, `"Fizz"`, `"Buzz"`, or the number as string. Print results for 1–20 space-separated.

Expected output:
```
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz
```

---

### Exercise 5: Loops

1. Print all even numbers from 2 to 20 inclusive, space-separated.
2. Compute and print first 10 Fibonacci numbers using `while`, space-separated.
3. Loop 1–20: skip multiples of 3 (`continue`), stop at first multiple of 7 (`break`). Print: `1 2 4 5`
4. Using `enumerate` and `zip` with `cities` and `populations` lists, print numbered comparison.

---

### Exercise 6: Functions

1. Write `temperature_convert(value, unit="C")` — converts C↔F, returns result rounded to 2 decimal places.
2. Write `summarize(*values)` — returns dict with `count`, `sum`, `min`, `max`, `mean`.
3. Write `format_record(**fields)` — returns `"key=value | key=value"` pairs sorted alphabetically.

---

### Exercise 7: Scope

1. Predict then verify output of LEGB example with nested `outer()` / `inner()` functions.
2. Write `increment_counter()` using `global` keyword. Call 3 times, print `counter` after each.
3. Write `make_multiplier(factor)` closure. Test `double = make_multiplier(2)`, `triple = make_multiplier(3)`.

---

## 8. WHAT HAS BEEN DONE SO FAR

| Date | Action |
|---|---|
| 2026-06-15 | Set up Python 3.14 environment on Windows |
| 2026-06-15 | Resolved PATH conflict with msys64 Python |
| 2026-06-15 | Created `Piscine_AI/python_basics/` directory |
| 2026-06-15 | This CLAUDE.md created |
| 2026-06-15 | Exercise 0 — venv creation in progress |

---

## 9. HOW TO IMPROVE THIS VAULT

Every session, Claude should ask: *"Did I learn something new about Kairo's learning style or environment today?"* If yes, update the relevant vault file. Over time this vault becomes a precise, personal knowledge base that makes every session faster and smarter than the last.

The vault is not optional. It is the memory layer that makes you useful across sessions.

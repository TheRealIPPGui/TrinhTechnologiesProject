# Python Skills Assessment — Personal Finance Tracker

**Assigned by:** Ryan Trinh, Trinh Technologies LLC  
**Purpose:** Evaluate Python fundamentals through a practical, staged project  

---

## Overview

Build a command-line personal finance tracker in Python. The application should allow a user to add expenses, view recorded expenses, generate a spending summary by category, and identify their top spending category — all through an interactive terminal menu.

This project is designed to test your ability to write clean, functional Python code using core language features: functions with proper signatures, data structures, control flow, string formatting, and error handling.

---

## Requirements

- Python 3.10+
- No external libraries — standard library only
- All code in a single file: `finance_tracker.py`
- The program should run from the terminal with `python finance_tracker.py`

---

## Stage 1 — Core Loop and Data Entry (Baseline)

Build the foundation: a menu-driven loop that lets the user add and view expenses.

**Implement the following:**

1. A `main()` function that runs a `while` loop displaying a numbered menu:
   - `1` — Add Expense
   - `2` — View All Expenses
   - `3` — Exit
2. A function `add_expense(expenses)` that:
   - Takes the expense list as a parameter
   - Prompts the user for an amount (float), category (string), and description (string)
   - Appends a dictionary `{"amount": ..., "category": ..., "description": ...}` to the list
   - Returns nothing (modifies the list in place)
3. A function `view_expenses(expenses)` that:
   - Takes the expense list as a parameter
   - Prints each expense in a readable format using f-strings
   - Handles the case where the list is empty (print a message, don't crash)

**Key constraints:**

- Every function must have parentheses, at least one parameter, and a colon in the `def` line
- Use `if/elif/else` to handle menu selection
- Store all expenses in a single list of dictionaries

**Done when:** You can add multiple expenses, view them all, and exit cleanly without errors.

---

## Stage 2 — Summary and Analysis

Add two functions that process the expense data and **return** values (not just print).

**Implement the following:**

1. A function `get_summary(expenses)` that:
   - Takes the expense list as a parameter
   - **Returns** a dictionary where keys are category names and values are total amounts for that category
   - Example return: `{"Food": 45.50, "Transport": 22.00, "Entertainment": 15.00}`
2. A function `get_top_category(summary)` that:
   - Takes the summary dictionary (output of `get_summary`) as a parameter
   - **Returns** a tuple of `(category_name, total_amount)` for the highest-spending category
   - Example return: `("Food", 45.50)`
3. Add two new menu options:
   - `3` — View Summary (calls `get_summary`, then prints the result)
   - `4` — View Top Category (calls `get_summary`, then `get_top_category`, then prints)
   - Move Exit to `5`

**Key constraints:**

- `get_summary` and `get_top_category` must use `return`, not `print` — the calling code in `main()` handles display
- This distinction between returning data and printing it is critical; do not conflate them

**Done when:** You can add several expenses across different categories, view a per-category breakdown, and see which category has the highest total.

---

## Stage 3 — Input Validation and Error Handling

Make the application robust against bad user input.

**Implement the following:**

1. Wrap the amount input in a `try/except` block:
   - If the user enters something that can't convert to `float`, print an error message and return to the menu (don't crash)
   - If the amount is negative or zero, reject it with a message
2. Handle empty string inputs for category and description (prompt again or use a default)
3. Handle invalid menu selections (anything outside the valid range prints a message and loops back)
4. Ensure `get_top_category` handles an empty expense list gracefully (return `None` or a message, don't crash)

**Key constraints:**

- The program should never crash from user input, no matter what is entered
- Use `try/except ValueError` specifically — not a bare `except`

**Done when:** You can mash random inputs at every prompt and the program handles all of them without a traceback.

---

## Stage 4 — File Persistence (Stretch)

Add the ability to save expenses to a file and load them on startup.

**Implement the following:**

1. A function `save_expenses(expenses, filename="expenses.json")` that:
   - Takes the expense list and a filename as parameters
   - Writes the list to a JSON file using the `json` module
   - Returns nothing
2. A function `load_expenses(filename="expenses.json")` that:
   - Takes a filename as a parameter
   - **Returns** the expense list loaded from the JSON file
   - If the file doesn't exist, **returns** an empty list (use `try/except FileNotFoundError`)
3. Call `load_expenses()` at the start of `main()` to initialize the list
4. Call `save_expenses()` after every new expense is added

**Key constraints:**

- Use `import json` — the `json.dump()` and `json.load()` functions
- Use `with open(...)` for file I/O (context managers)
- The `load_expenses` function must handle the missing file case without crashing

**Done when:** You can add expenses, close the program, reopen it, and see your previous expenses still there.

---

## Submission Checklist

Before submitting, verify:

- [ ] Every `def` line has parentheses, parameter(s), and a colon
- [ ] Functions that compute results use `return`, not `print`
- [ ] Functions that display output use `print` and don't `return` the display string
- [ ] All menu branching uses `if/elif/else` with proper colons
- [ ] No bare `except:` blocks — always catch specific exceptions
- [ ] The program handles all invalid inputs without crashing
- [ ] Code runs with `python finance_tracker.py` with no modifications

---

## Grading Criteria

| Criteria | Weight |
|---|---|
| Stage 1 — Core loop, menu, add/view functions | 25% |
| Stage 2 — Summary and top category with proper `return` usage | 25% |
| Stage 3 — Input validation and error handling | 25% |
| Stage 4 — JSON persistence with file I/O | 15% |
| Code quality — naming, readability, no shadowed built-ins | 10% |

**Automatic deductions:**

- Using `print` where `return` is required: **-5% per occurrence**
- Missing parentheses or parameters on any `def` line: **-5% per occurrence**
- Bare `except:` without a specific exception type: **-3% per occurrence**
- Program crashes on any reasonable input: **-5% per crash scenario**

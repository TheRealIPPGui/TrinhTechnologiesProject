# Code Review Grade 4/18/2026
## By Chase Wasalaski

## Project Requirements (40 / 50)

*Aligned with `instructions.md`: stages, constraints, and submission expectations.*

### Stage 1 — Core loop, menu, add/view (11 / 12)

Mostly good, multiple inputs can sometimes be awkward but functional and useable

### Stage 2 — Summary, top category, return vs print (10 / 12)

Functionally works, json output is unappealing

### Stage 3 — Input validation and error handling (10 / 13)

One crash, see below

### Stage 4 — JSON persistence (4 / 8)

Functionality is there, just not used or is not working properly
No file / JSON persistence

### Global constraints & submission (5 / 5)

#### Single file, entrypoint, standard library only (2 / 2)

#### Function signatures and menu branching (`if` / `elif` / `else`) (2 / 2)

Note: This code segment doesn't need a parameter

```
def get_summary(expenses):
        if summary == {}:
             print("There is nothing to display!")
             input("Press Enter to continue...")
        else:
            
            
           
            return(summary)
```

#### Data model: single list of expense dictionaries (1 / 1)

---

## Code Review (40 / 50)

*Quality and engineering judgment beyond checklist compliance — not a repeat of the project spec.*

### Structure and separation of concerns (12 / 12)

### Naming, readability, and consistency (6 / 12)

-2 Tab Consistency
Sometimes multiple tabs where one is required
Important in Python because its literally syntax

-1 Unnecessary Code

if amount == float is handled by the try except ValueError
```py
try:
    amount = float(input("Please enter the expense amount: \n"))
    if amount == float:
        while amount < 0:
            print("This value cannot be 0")
            amount = float(input("Please enter the expense amount: \n"))
                
except ValueError:
    print("Please enter a positive number!")
```

-1 General Readability and Spacing

Large whitespace or no whitespace at all.
This makes it especially hard to follow code in complicated branches.

-1 Loop Variables

Loop Variables are not named well, it is difficult to tell what this flow is doing at a glance, same with global variables

```py
for k, v in summary.items():
    global mv
    if v > mv:
        mv = v
        mk = k
print(f"The top category is {mk} with the total being {mv}")
```

-1 Point

Displays the category as an array

```
PornHub was an expense of 100.0 dollars, inside the ['subscriptions'] category, and having a description of: Stroking my cock
```

### Control flow clarity and logical organization (8 / 10)

-1 Unhandled catch

Error is ignored instead of handled accordingly, you could also error here in the save_expenses function and it won't catch it since you only catch UnboundLocalError

```py
try:
    expenses.update({expense_name: {"amount": amount, "category": [category], "description": description}})
    save_expenses(expenses, filename="expenses.json")

except UnboundLocalError:
    pass
```

-1 Out of order control flow
Flow in the main function goes 1 2 5 3 4

### Idiomatic Python and appropriate use of language features (8 / 8)

### Comments, docstrings, and explainability (where helpful) (4 / 5)

-1 Comments are misaligned with code making it hard to follow where the comments point

### Maintainability — avoid unnecessary complexity; sensible decomposition (2 / 3)

-1 No utility functions / reused code
Code can be reused in multiple places, ie invalid input handling

---

## Automatic deductions (from instructions)

*Apply as negative adjustments to the **Project Requirements** subtotal or overall total per your policy.*

- Using `print` where `return` is required: **−5% per occurrence** (of applicable component or whole grade — specify in scorer notes)
- Missing parentheses or parameters on any `def` line: **−5% per occurrence**
- Bare `except:` without a specific exception type: **−3% per occurrence**
- Program crashes on reasonable input: **−5% per crash scenario**

Crash

Viewing top category twice after adding an expense crashes program
```
To choose an option, please enter an value 1-5
4
The top category is subscriptions with the total being 100.0
None
Welcome to the menu!
Option 1 - Add Expenses
Option 2 - View All Expenses
Option 3 - View Summary
Option 4 - View Top Category
Option 5 - Exit
To choose an option, please enter an value 1-5
4
Traceback (most recent call last):
  File "C:\Users\chase\OneDrive\Desktop\Programming\LiamFi\TrinhTechnologiesProject\finance_tracker.py", line 147, in <module>
    main()
  File "C:\Users\chase\OneDrive\Desktop\Programming\LiamFi\TrinhTechnologiesProject\finance_tracker.py", line 134, in main
    print(get_top_category(summary))
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\chase\OneDrive\Desktop\Programming\LiamFi\TrinhTechnologiesProject\finance_tracker.py", line 75, in get_top_category
    print(f"The top category is {mk} with the total being {mv}")
                                 ^^
UnboundLocalError: cannot access local variable 'mk' where it is not associated with a value
```
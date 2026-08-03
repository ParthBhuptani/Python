# 15-Day Python Workbook
### From Zero to Confident Beginner

This workbook takes you from installing Python to building a small real project in 15 focused days. Each day includes: **Learning Objectives**, **Theory**, **Hands-On Exercises**, **Coding Tasks**, a **Mini Assignment**, **Revision Questions**, and an **End-of-Day Challenge**.

**How to use this workbook:**
- Spend 45–90 minutes per day.
- Type every example yourself — don't copy-paste. Typing builds muscle memory.
- Don't move to the next day until you can answer the revision questions without looking back.
- Keep a folder called `python_workbook/day01`, `day02`, etc., and save your work there.

---

## Day 1 — Getting Started with Python

**Learning Objectives**
- Install Python and run your first program
- Understand what an interpreter does
- Use `print()` and comments

**Theory**
Python is an interpreted, high-level programming language, meaning code runs line by line without a separate compile step. You write code in `.py` files and run them with the `python` (or `python3`) command. Comments (`#`) are ignored by the interpreter and exist purely to explain code to humans.

**Hands-On Exercises**
1. Install Python from python.org and confirm with `python --version` in your terminal.
2. Create `hello.py` containing `print("Hello, World!")` and run it.
3. Add a comment above the print line explaining what it does.
4. Print your name and age on two separate lines.
5. Try `print("A", "B", "C", sep=" - ")` and observe the `sep` argument.

**Coding Task**
Write a script `intro.py` that prints a short 4-line bio about yourself (name, hobby, favorite food, one goal for learning Python).

**Mini Assignment**
Write a program that prints a simple ASCII art box (using `-` and `|`) around the text "PYTHON JOURNEY".

**Revision Questions**
1. What is the difference between a compiled and an interpreted language?
2. What symbol starts a comment in Python?
3. What does `print()` do?
4. What is the file extension for Python scripts?

**End-of-Day Challenge**
Write a program that prints a multiplication fact using only `print()` statements (e.g., "7 times 8 is 56") — without doing the math in your head; just print literal text for now (real math comes on Day 3).

---

## Day 2 — Variables and Data Types

**Learning Objectives**
- Create and name variables correctly
- Understand core data types: `int`, `float`, `str`, `bool`
- Convert between types (type casting)

**Theory**
A variable is a named label pointing to a value in memory, created with `name = value`. Python is dynamically typed — you don't declare a type, Python infers it. Core built-in types include whole numbers (`int`), decimals (`float`), text (`str`), and true/false values (`bool`). Use `type(x)` to check a variable's type, and functions like `int()`, `str()`, `float()` to convert between types.

**Hands-On Exercises**
1. Create variables for your `name`, `age`, `height_m`, and `is_student`, then print each with `type()`.
2. Convert the string `"25"` into an integer and add 5 to it.
3. Convert an integer into a string and concatenate it with text.
4. Try adding a string and an integer directly and observe the error.
5. Use `input()` to ask the user's name and greet them.

**Coding Task**
Write `profile.py` that asks the user for their name, age, and city via `input()`, then prints a formatted sentence using an f-string, e.g., `f"{name} is {age} years old and lives in {city}."`

**Mini Assignment**
Write a program that takes a temperature in Celsius (as input, a string) and converts it to Fahrenheit, printing the result with one decimal place.

**Revision Questions**
1. What's the difference between `int`, `float`, and `str`?
2. Why does `"5" + 5` raise an error?
3. What does `type()` return?
4. What does dynamically typed mean?

**End-of-Day Challenge**
Write a program that stores your favorite three numbers in three variables, then prints their sum, average, and which one is largest — without using lists (that's Day 5).

---

## Day 3 — Operators and Expressions

**Learning Objectives**
- Use arithmetic, comparison, and logical operators
- Understand operator precedence
- Build compound expressions

**Theory**
Arithmetic operators (`+ - * / // % **`) perform math; `/` always returns a float, `//` does floor (integer) division, and `%` gives the remainder. Comparison operators (`== != > < >= <=`) return booleans. Logical operators (`and`, `or`, `not`) combine boolean expressions. Precedence rules determine order of evaluation — parentheses always win.

**Hands-On Exercises**
1. Compute `17 // 5` and `17 % 5` and explain the results in a comment.
2. Compute `2 ** 10` and print it.
3. Compare two numbers with `>` and `and` them with a boolean check.
4. Predict then verify the result of `3 + 4 * 2` vs `(3 + 4) * 2`.
5. Write an expression using `not` to flip a boolean.

**Coding Task**
Write `calculator.py` that takes two numbers and an operator symbol (`+ - * /`) as input and prints the result, handling division by zero with a friendly message (a simple `if` check is fine here).

**Mini Assignment**
Write a program that checks if a year (input as a number) is a leap year, using `%` and logical operators, printing `True` or `False`.

**Revision Questions**
1. What's the difference between `/` and `//`?
2. What does `%` return?
3. What does `and` require to be `True`?
4. Why does precedence matter in `3 + 4 * 2`?

**End-of-Day Challenge**
Write a program that takes three side lengths as input and prints whether they could form a valid triangle (sum of any two sides must exceed the third), using only comparison and logical operators.

---

## Day 4 — Strings and String Methods

**Learning Objectives**
- Slice and index strings
- Use common string methods
- Format strings with f-strings

**Theory**
Strings are sequences of characters, indexable with `[]` (starting at 0) and sliceable with `[start:stop:step]`. Strings are immutable — methods like `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, and `.join()` return *new* strings rather than modifying the original. f-strings (`f"{variable}"`) are the modern way to embed values into text.

**Hands-On Exercises**
1. Given `s = "Python Programming"`, print the first 6 characters, then the last 11.
2. Reverse `s` using slicing (`s[::-1]`).
3. Use `.split()` to break a sentence into a list of words.
4. Use `.join()` to combine a list of words back into a sentence.
5. Use `.replace()` to censor a word in a sentence.

**Coding Task**
Write `word_stats.py` that takes a sentence as input and prints: number of characters, number of words, and the sentence in all uppercase.

**Mini Assignment**
Write a palindrome checker: given a word, print whether it reads the same forwards and backwards (ignore case).

**Revision Questions**
1. Why are strings called "immutable"?
2. What does `s[::-1]` do?
3. What's the difference between `.split()` and `.join()`?
4. How do f-strings differ from regular string concatenation?

**End-of-Day Challenge**
Write a simple Caesar cipher: shift every letter in a word forward by 1 in the alphabet (e.g., "abc" → "bcd"), printing the encoded result. (Hint: look up `ord()` and `chr()`.)

---

## Day 5 — Lists

**Learning Objectives**
- Create, index, and slice lists
- Add, remove, and modify list items
- Iterate over a list

**Theory**
A list is an ordered, mutable collection written with `[]`. Unlike strings, lists can be changed in place: `.append()` adds to the end, `.remove()` deletes a value, `.pop()` removes by index, and `.sort()` orders items. Lists can hold mixed types and can be nested.

**Hands-On Exercises**
1. Create a list of 5 fruits and print the 2nd and last item.
2. Append a new fruit, then remove one by name.
3. Sort the list alphabetically and then reverse it.
4. Use a `for` loop (preview) to print each fruit on its own line: `for fruit in fruits: print(fruit)`.
5. Check if an item exists using `in`.

**Coding Task**
Write `todo_list.py` that starts with an empty list, adds 5 tasks via `.append()`, prints them numbered (1., 2., ...), then removes the 3rd task and reprints the list.

**Mini Assignment**
Write a program that takes a list of numbers (hardcoded) and prints the largest, smallest, and their sum without using `max()`, `min()`, or `sum()` — use a loop and comparisons instead.

**Revision Questions**
1. What makes lists "mutable"?
2. What's the difference between `.remove()` and `.pop()`?
3. How do you check if an item is in a list?
4. Can a list contain different data types at once?

**End-of-Day Challenge**
Write a program that removes duplicate values from a list while keeping the original order, without using `set()` (loop through and build a new list).

---

## Day 6 — Tuples and Sets

**Learning Objectives**
- Understand tuples as immutable sequences
- Understand sets as unordered, unique collections
- Know when to use list vs tuple vs set

**Theory**
A tuple `()` is like a list but immutable — useful for fixed data (e.g., coordinates). A set `{}` stores unique, unordered items and supports mathematical operations like union (`|`), intersection (`&`), and difference (`-`). Choosing the right structure matters: use tuples for fixed records, sets for uniqueness checks, and lists for ordered, changeable collections.

**Hands-On Exercises**
1. Create a tuple `point = (3, 4)` and try to change one value — observe the error.
2. Unpack a tuple into two variables: `x, y = point`.
3. Create two sets of numbers and find their union and intersection.
4. Convert a list with duplicates into a set to remove duplicates.
5. Check membership (`in`) in a set vs a list — note sets are faster for this.

**Coding Task**
Write `contacts.py` using a list of tuples `[("Alice", "555-1111"), ("Bob", "555-2222")]` and print each contact formatted as `Name: Phone`.

**Mini Assignment**
Write a program with two sets of student names (Math class, Science class) and print: students in both classes, students only in Math, and all students combined.

**Revision Questions**
1. Why can't you change a tuple after creating it?
2. What happens if you add a duplicate value to a set?
3. When would you choose a tuple over a list?
4. What operator finds the intersection of two sets?

**End-of-Day Challenge**
Write a program that takes two lists of numbers and prints which values appear in both, using sets, without any explicit loops.

---

## Day 7 — Dictionaries

**Learning Objectives**
- Create and access key-value pairs
- Add, update, and remove entries
- Iterate over keys, values, and items

**Theory**
A dictionary `{}` maps unique keys to values, giving fast lookups by key instead of position. Access with `d[key]` or safely with `d.get(key, default)`. Use `.keys()`, `.values()`, and `.items()` to iterate. Dictionaries are the backbone of representing structured, real-world data in Python.

**Hands-On Exercises**
1. Create a dictionary of a person's `name`, `age`, `city` and print each value.
2. Add a new key `email` and update the `age`.
3. Delete a key with `del` or `.pop()`.
4. Loop over `.items()` and print `"key: value"` for each pair.
5. Use `.get()` to safely access a missing key with a default value.

**Coding Task**
Write `inventory.py` with a dictionary mapping product names to prices. Ask the user for a product name and print its price, or "Not found" using `.get()`.

**Mini Assignment**
Write a word-frequency counter: given a sentence, build a dictionary counting how many times each word appears, then print it sorted by count (highest first).

**Revision Questions**
1. Why must dictionary keys be unique?
2. What's the difference between `d[key]` and `d.get(key)`?
3. What three methods let you loop over a dictionary?
4. Can a dictionary value be a list? Can it be another dictionary?

**End-of-Day Challenge**
Build a simple phonebook program: a dictionary of names/numbers where the user can choose to add, look up, or delete a contact via `input()`, in a single run (no loop needed yet — that's Day 9).

---

## Day 8 — Conditional Logic (if / elif / else)

**Learning Objectives**
- Control program flow with conditionals
- Nest and chain conditions correctly
- Combine conditionals with logical operators

**Theory**
`if`, `elif`, and `else` let a program make decisions by running different code blocks depending on whether conditions are true. Indentation (4 spaces) defines what belongs to each block — this is not optional in Python. Conditions can be combined with `and`/`or`/`not`, and nested for multi-layered logic.

**Hands-On Exercises**
1. Write an `if/else` that prints "Even" or "Odd" for a number.
2. Write an `if/elif/else` chain that grades a score: A (90+), B (80+), C (70+), else F.
3. Nest an `if` inside another `if` to check two conditions.
4. Combine two conditions with `and` in a single `if`.
5. Rewrite an `if/elif` chain using only `and`/`or` in one condition where possible.

**Coding Task**
Write `login_check.py` that stores a correct username and password as variables, asks the user to input both, and prints "Access granted" or "Access denied" accordingly.

**Mini Assignment**
Write a simple BMI category checker: given weight and height as input, compute BMI and print the category (Underweight/Normal/Overweight/Obese) using standard BMI ranges.

**Revision Questions**
1. Why does indentation matter in Python conditionals?
2. What's the difference between `elif` and a separate `if`?
3. How do you check two conditions must both be true?
4. What happens if no condition in an `if/elif` chain is true and there's no `else`?

**End-of-Day Challenge**
Write a simple rock-paper-scissors judge: given two inputs (player choices), print who wins using nested/combined conditionals — no randomness yet (that comes with modules later).

---

## Day 9 — Loops (for and while)

**Learning Objectives**
- Automate repetition with `for` and `while`
- Use `range()`, `break`, and `continue`
- Avoid infinite loops

**Theory**
`for` loops iterate over a known sequence (list, string, `range()`), while `while` loops repeat as long as a condition holds — useful when the number of repetitions isn't known ahead of time. `break` exits a loop early; `continue` skips to the next iteration. A `while` loop needs its condition to eventually become false, or it runs forever.

**Hands-On Exercises**
1. Use `for i in range(1, 11)` to print numbers 1–10.
2. Use a `for` loop to print only even numbers from 1–20 using `continue`.
3. Use a `while` loop to count down from 10 to 1.
4. Use `break` to stop a loop as soon as a target number is found in a list.
5. Loop over a string, printing each character on its own line.

**Coding Task**
Write `guess_game.py`: store a secret number, then use a `while` loop that keeps asking the user to guess until they get it right, telling them "Too high" or "Too low" each time.

**Mini Assignment**
Write a program that uses a `for` loop to build the multiplication table (1–12) for a number the user provides.

**Revision Questions**
1. When would you choose `while` over `for`?
2. What does `break` do differently from `continue`?
3. What causes an infinite loop, and how do you fix one?
4. What does `range(2, 10, 2)` produce?

**End-of-Day Challenge**
Write a program that checks whether a number is prime using a `for` loop and `break` to stop checking as soon as a factor is found.

---

## Day 10 — Functions: The Basics

**Learning Objectives**
- Define and call functions with `def`
- Use parameters, arguments, and return values
- Understand variable scope

**Theory**
Functions package reusable logic under a name using `def name(parameters):`. `return` sends a value back to the caller; a function without `return` implicitly returns `None`. Variables defined inside a function (local scope) are separate from variables outside it (global scope) unless explicitly declared `global`.

**Hands-On Exercises**
1. Write a function `greet(name)` that returns a greeting string.
2. Write a function `square(n)` that returns `n * n`.
3. Write a function with a default parameter value, e.g. `greet(name="friend")`.
4. Try printing a variable defined inside a function from outside it — observe the error.
5. Write a function that returns two values as a tuple, then unpack them when calling.

**Coding Task**
Write `temp_converter.py` with two functions, `c_to_f(c)` and `f_to_c(f)`, and a small menu using `input()` to let the user pick a conversion.

**Mini Assignment**
Write a function `is_palindrome(word)` that returns `True`/`False`, then test it against at least 5 words including edge cases (empty string, single letter).

**Revision Questions**
1. What's the difference between a parameter and an argument?
2. What does a function return if there's no `return` statement?
3. What is variable scope, and why does it matter?
4. Why are default parameter values useful?

**End-of-Day Challenge**
Write a function `stats(numbers)` that takes a list and returns a dictionary with `min`, `max`, and `average` — then call it on three different lists.

---

## Day 11 — Functions: Going Further

**Learning Objectives**
- Use `*args` and `**kwargs`
- Write and use lambda functions
- Understand recursion basics

**Theory**
`*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dictionary — both let functions accept a flexible number of inputs. A `lambda` is a small, unnamed function for short expressions, often used with functions like `sorted()` or `map()`. Recursion is when a function calls itself, always needing a base case to stop.

**Hands-On Exercises**
1. Write `add_all(*args)` that returns the sum of any number of arguments.
2. Write a function using `**kwargs` that prints each keyword and value passed in.
3. Write a `lambda` that doubles a number and call it directly.
4. Use `sorted()` with a `key=lambda` to sort a list of tuples by their second element.
5. Write a recursive function `countdown(n)` that prints numbers down to 0.

**Coding Task**
Write `factorial.py` with a recursive function `factorial(n)` and an iterative function `factorial_loop(n)`, printing both results for a few test values to confirm they match.

**Mini Assignment**
Write a function `describe_person(name, **kwargs)` that prints the name plus any extra details passed in (age, city, job, etc.) — call it with different combinations of keyword arguments.

**Revision Questions**
1. What's the difference between `*args` and `**kwargs`?
2. When is a `lambda` more appropriate than a regular function?
3. What must every recursive function have to avoid infinite recursion?
4. What data type does `**kwargs` collect arguments into?

**End-of-Day Challenge**
Write a recursive function to compute the nth Fibonacci number, then compare its speed conceptually to an iterative version (no need to benchmark — just reason about it in a comment).

---

## Day 12 — Error Handling

**Learning Objectives**
- Handle runtime errors gracefully with try/except
- Raise custom errors
- Use finally for cleanup logic

**Theory**
Errors (exceptions) stop a program unless caught. `try/except` lets you catch specific exception types (like `ValueError`, `ZeroDivisionError`) and respond gracefully instead of crashing. `finally` runs no matter what, useful for cleanup. You can also `raise` your own exceptions when input is invalid for your program's logic.

**Hands-On Exercises**
1. Wrap `int(input())` in a `try/except` to catch a `ValueError` if the user types letters.
2. Catch a `ZeroDivisionError` when dividing by a user-provided number.
3. Use `except Exception as e:` and print the error message.
4. Add a `finally` block that always prints "Done" regardless of errors.
5. Use `raise ValueError("message")` inside a function when an invalid argument is passed.

**Coding Task**
Write `safe_calculator.py` that repeatedly (using a loop) asks for two numbers and an operator, catching invalid input and division by zero without crashing, until the user types "quit".

**Mini Assignment**
Write a function `get_positive_number()` that keeps asking the user for input until they provide a valid positive number, using `try/except` and a loop together.

**Revision Questions**
1. What's the difference between an error and an exception in everyday Python usage?
2. Why catch specific exceptions instead of a bare `except:`?
3. When does the `finally` block run?
4. When would you deliberately `raise` an exception in your own code?

**End-of-Day Challenge**
Write a small "input validator" function that checks an email string has an "@" and a "." after it, raising a custom `ValueError` with a clear message if not.

---

## Day 13 — Working with Files

**Learning Objectives**
- Read from and write to text files
- Use `with` for safe file handling
- Process file content line by line

**Theory**
Files are opened with `open(path, mode)` where mode is `"r"` (read), `"w"` (write, overwrites), or `"a"` (append). The `with open(...) as f:` pattern automatically closes the file even if an error occurs, which is why it's preferred over manually calling `.close()`. Files can be read fully with `.read()`, line by line with `.readline()` or a `for` loop, or as a list of lines with `.readlines()`.

**Hands-On Exercises**
1. Write a few lines of text to a new file using `"w"` mode.
2. Read the whole file back with `.read()` and print it.
3. Append an additional line using `"a"` mode.
4. Loop over the file line by line, printing each line without extra blank lines (`.strip()`).
5. Count how many lines are in the file.

**Coding Task**
Write `notes_app.py` that lets the user add a note (appended to `notes.txt` with a timestamp-like label) and view all saved notes, using a simple menu with `input()`.

**Mini Assignment**
Write a program that reads a text file and writes a new file containing only the lines that include a specific keyword provided by the user.

**Revision Questions**
1. Why is `with open(...)` preferred over `open()` alone?
2. What's the difference between `"w"` and `"a"` modes?
3. What does `.readlines()` return?
4. What happens if you open a file that doesn't exist in `"r"` mode?

**End-of-Day Challenge**
Write a simple line-count, word-count, and character-count tool for any `.txt` file, printing all three statistics.

---

## Day 14 — Modules and Intro to Object-Oriented Programming

**Learning Objectives**
- Import and use standard library modules
- Organize code into your own modules
- Create basic classes with attributes and methods

**Theory**
Modules are files of reusable code; import the standard library with `import module_name` (e.g., `random`, `math`, `datetime`) or your own files the same way. Classes (`class Name:`) are blueprints for creating objects that bundle data (attributes) and behavior (methods) together. The `__init__` method runs automatically when an object is created, and `self` refers to the specific object being worked with.

**Hands-On Exercises**
1. Import `random` and generate a random number between 1 and 100.
2. Import `math` and use `math.sqrt()` and `math.pi`.
3. Create your own file `helpers.py` with one function, then import and use it from another file.
4. Define a class `Dog` with `__init__(self, name, breed)` and a method `bark(self)`.
5. Create two `Dog` objects with different data and call `.bark()` on each.

**Coding Task**
Write a `BankAccount` class with `__init__(self, owner, balance=0)`, and methods `deposit(amount)`, `withdraw(amount)` (rejecting overdraws), and `show_balance()`.

**Mini Assignment**
Extend the `Dog` class with an attribute `age` and a method `birthday()` that increases age by 1 and prints a message — create three dogs and simulate a birthday for each.

**Revision Questions**
1. What's the difference between a module and a package?
2. What does `self` represent inside a class?
3. When does `__init__` run?
4. Why organize code into your own modules instead of one huge file?

**End-of-Day Challenge**
Rebuild the Day 9 guessing game as a `GuessingGame` class, with attributes for the secret number and attempt count, and a method `guess(number)` that returns feedback — this bridges loops, functions, and OOP together.

---

## Day 15 — Capstone Project: Putting It All Together

**Learning Objectives**
- Combine variables, loops, conditionals, functions, dictionaries, files, and classes into one project
- Practice planning a program before coding it
- Debug and refine a multi-part application

**Theory**
Real programs aren't single concepts in isolation — they're combinations of everything you've learned. Today is about *synthesis*: planning your program's structure first (what data do I need? what functions? what's the user flow?), then building it piece by piece, testing as you go rather than writing everything at once.

**Project: Personal Expense Tracker**
Build a command-line app that:
1. Stores expenses as a list of dictionaries, e.g. `{"item": "Coffee", "amount": 4.5, "category": "Food"}`.
2. Offers a menu (loop until user quits): Add expense, View all expenses, View total by category, Save to file, Load from file, Exit.
3. Uses functions for each menu action (`add_expense()`, `view_total_by_category()`, etc.).
4. Saves/loads data to/from a text or CSV file so expenses persist between runs.
5. Handles bad input gracefully (e.g., entering text where a number is expected) using `try/except`.
6. Optionally wraps the whole tracker in an `ExpenseTracker` class as a stretch goal.

**Hands-On Build Steps**
1. Sketch the menu and data structure on paper first.
2. Build the "Add expense" and "View all" features and test them.
3. Add category totals using a dictionary to accumulate sums.
4. Add file save/load.
5. Add error handling last, once the happy path works.

**Mini Assignment**
Add a feature to filter and display expenses above a certain amount, entered by the user.

**Revision Questions**
1. Which three data structures did you rely on most in this project, and why?
2. Where did you use functions to avoid repeating code?
3. What was the trickiest bug you hit, and how did you find it?
4. If you rebuilt this project as a class, what would the attributes and methods be?

**Final Challenge**
Add a simple report feature: print total spending, the single largest expense, and the category with the highest spend — formatted neatly with headers and separators (`"-" * 30`, etc.).

**Congratulations!** You've gone from `print("Hello, World!")` to a multi-feature program using variables, control flow, functions, data structures, files, error handling, and classes. From here, natural next steps include: list/dict comprehensions, virtual environments, `pip` and third-party packages, and building a small web app or automation script.

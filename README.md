# Python Learning Journey

A day-by-day Python practice repository covering core programming concepts, problem-solving exercises, object-oriented programming, advanced Python features, and small beginner-friendly projects.

This repository is organized as a structured learning log, with each `DayXX` folder containing Python scripts, notes, examples, and supporting assets from that day.

## Repository Overview

```text
Python/
|-- Day01/   Python basics, modules, and directory listing
|-- Day02/   Input handling, type casting, strings, and formatting
|-- Day03/   Conditional statements, loops, and PIN-style logic
|-- Day04/   Number swapping program
|-- Day05/   Lists, tuples, slicing, and indexing
|-- Day06/   Sets, dictionaries, and membership operations
|-- Day07/   Functions, arguments, and keyword arguments
|-- Day08/   Nested loops, patterns, split input, and comprehensions
|-- Day09/   Exception handling with try, except, else, and finally
|-- Day10/   File handling, conversions, and high-score file updates
|-- Day11/   Recursion and object-oriented programming
|-- Day12/   Lambda functions, comprehensions, typing, and match-case
|-- Day13/   Map, filter, reduce, and number guessing game
|-- Day14/   Iterator and generator notes
`-- Day15/   Snake game using Turtle
```

## Topics Covered

- Python syntax and program structure
- Variables, data types, and type casting
- Input/output and formatted strings
- Strings, slicing, and common string methods
- Conditional statements and loops
- Lists, tuples, sets, and dictionaries
- Functions, default arguments, `*args`, and `**kwargs`
- Pattern printing and nested loops
- Exception handling
- File reading, writing, and high-score tracking
- Recursion with factorial and Fibonacci examples
- Object-oriented programming
- Constructors, static methods, class methods, and properties
- Inheritance, `super()`, and operator overloading
- Lambda functions, list comprehension, and `enumerate`
- Type hints using `typing`
- Dictionary merge operator and multiple context managers
- `match-case` control flow
- Functional programming with `map`, `filter`, and `reduce`
- Beginner game development with `turtle`

## Day-Wise Progress

| Day | Main Files | Focus Area |
| --- | --- | --- |
| Day01 | `python.py`, `me.py`, `content_of_directory.py` | Python basics, text-to-speech module usage, variables, data types, comments, printing, and listing directory contents with `os`. |
| Day02 | `me.py` | User input, type casting, memory identity with `id()`, string slicing, string methods, f-strings, and string replacement. |
| Day03 | `python.py` | `if`, `else`, `elif`, `for` loops, `range()`, `while-else`, and PIN verification style logic. |
| Day04 | `python.py` | Swapping two numbers using a temporary variable. |
| Day05 | `python.py` | Lists, tuples, slicing, negative indexing, tuple-to-list conversion, sorting, and counting tuple values. |
| Day06 | `python.py` | Set operations, dictionary methods, subset/superset checks, empty sets, and membership testing with `in`. |
| Day07 | `python.py` | Function creation, function calls, addition function, default arguments, variable-length arguments, and keyword arguments. |
| Day08 | `python.py` | Nested loops, pattern printing, `pass`, input splitting, list/tuple/dictionary input building, and comprehension-style input conversion. |
| Day09 | `python.py` | Exception handling using `try`, `except`, `else`, `finally`, multiple exceptions, and manual error raising with `ValueError`. |
| Day10 | `python.py`, `test.py`, `hiscore.txt`, `myfile.txt` | File handling, reading lines, writing files, Fahrenheit-to-Celsius conversion, inch-to-centimeter conversion, and high-score tracking. |
| Day11 | `python.py`, `OOPs*.py` | Recursion, factorial, Fibonacci, classes, objects, attributes, methods, constructors, inheritance, class methods, properties, and operator overloading. |
| Day12 | `python.py`, `advPython.py`, `advPython02.py` | Lambda functions, list comprehensions, `enumerate`, type hints, `Union`, dictionary merging, context managers, global variables, `join()`, and `match-case`. |
| Day13 | `python.py`, `Guess_The_Number.py` | Functional programming with `map`, `filter`, `reduce`, and a random number guessing game. |
| Day14 | `python.py` | Iterator and generator notes started. |
| Day15 | `Snake_Game.py` | A playable Snake game built with Python's `turtle` module, including movement, food, score, high score, and collision handling. |

## Featured Projects

### Guess The Number

Located in `Day13/Guess_The_Number.py`.

A simple terminal-based guessing game where the computer generates a random number from 1 to 100 and the player keeps guessing until the correct number is found.

```bash
python Day13/Guess_The_Number.py
```

### Snake Game

Located in `Day15/Snake_Game.py`.

A graphical Snake game built with the `turtle` module. It includes keyboard controls, food spawning, score tracking, high-score tracking, body growth, border wrapping, and self-collision reset behavior.

```bash
python Day15/Snake_Game.py
```

## How To Run

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Python
   ```

2. Run any Python file:

   ```bash
   python Day01/me.py
   ```

3. For scripts inside folders, run them from the repository root so relative file paths work correctly:

   ```bash
   python Day10/python.py
   ```

## Requirements

Most examples use Python's standard library.

Recommended:

- Python 3.10 or newer
- `pyttsx3` for the text-to-speech example in `Day01/python.py`

Install optional dependency:

```bash
pip install pyttsx3
```

## Notes

- Some folders contain image files used as learning references or screenshots.
- Some scripts are interactive and require keyboard input in the terminal.
- File-handling examples may read or write local text files.
- The repository is intentionally organized as a learning timeline, so earlier days contain beginner syntax and later days introduce more advanced concepts.

## Future Improvements

- Add more mini projects for practice.
- Add comments and docstrings to project files.
- Separate concept notes from runnable programs.
- Add requirements file for external dependencies.
- Add screenshots or GIFs for visual projects such as the Snake game.

## Author

Maintained by Piyush as part of a hands-on Python learning journey.

# Expression Evaluator

A Python-based expression evaluator that calculates arithmetic expressions entered by the user and displays the result.

## Version

**Current version: 1.0**

Version 1.0 provides basic arithmetic expression evaluation, operator precedence handling, and error handling.

Future versions may introduce additional features, improved input validation, and support for more complex mathematical expressions.

## Features

- **Supported operators:** `**`, `^`, `//`, `*`, `/`, `%`, `+`, `-`
- Supports decimal numbers and negative numbers.
- Handles errors such as division by zero, invalid expressions, and empty input.
- Evaluates expressions according to operator precedence and associativity rules.

## Operator Precedence

The evaluator follows these operator precedence rules, from highest to lowest:

1. **Exponentiation:** `**`, `^`
   - Evaluated from right to left.
   - Example: `2**3**2` → `2**(3**2)` → `512`

2. **Multiplication, Division, Floor Division, and Modulo:** `*`, `/`, `//`, `%`
   - Operators of the same precedence are evaluated from left to right.
   - Example: `8/4*2` → `(8/4)*2` → `4`

3. **Addition and Subtraction:** `+`, `-`
   - Operators of the same precedence are evaluated from left to right.
   - Example: `10-3+2` → `(10-3)+2` → `9`

## Requirements

- Python 3 (use a version you have tested).
- A Python interpreter. You can use Python IDLE, VS Code, or a terminal.

## Installation and Usage

1. Download or clone the repository.
2. Navigate to the project folder.
3. Run `main.py` using Python.
4. Enter an arithmetic expression when prompted.

For example, from a terminal:

```bash
python main.py
```

## Example

**Input:**

```text
2**2**3+10//4-1
```

**Output:**

```text
257
```

## Project Structure

- **`tokenizer.py`** — Converts the input expression into a sequence of numbers and operators for the evaluator to process.
- **`evaluator.py`** — Evaluates the tokenized expression according to the implemented operator precedence and associativity rules.
- **`main.py`** — Accepts user input, calls the tokenizer and evaluator, handles errors, and displays the result.

## Limitations

- Parentheses are not supported.
- Mathematical functions such as `sin`, `cos`, `tan`, and `log` are not supported.

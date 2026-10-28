# Mini Language + Static Checker

A simple educational project that implements a tiny programming language with:

- Lexer (Tokenizer)
- Parser (Recursive Descent)
- Abstract Syntax Tree (AST)
- Static Checker (simple verifier)
- Optional Interpreter

This project demonstrates core ideas from **Programming Languages**, **Compilers**, and **Formal Methods**.

---

## Language Features

Supported statements:

```text
var x;              // variable declaration
x = 10;             // assignment
y = x + 5 * 2;      // arithmetic expression
print y;            // print statement
```

Supported operators: `+`, `-`, `*`, `/`  
Parentheses are allowed for grouping.

---

## What the Static Checker Detects

1. **Variable used before declaration**
2. **Variable declared more than once**
3. **Division by zero** (when the divisor is a constant 0)

---

## How to Run

```bash
# Only perform static checking
python main.py examples/correct1.mini

# Check + Execute the program
python main.py examples/correct1.mini --run
```

---

## Project Structure

```text
mini_lang_project/
├── main.py              # Entry point
├── lexer.py             # Tokenizer
├── parser.py            # Recursive Descent Parser
├── ast_nodes.py         # AST node definitions
├── checker.py           # Static Checker / Simple Verifier
├── interpreter.py       # Optional interpreter
├── examples/
│   ├── correct1.mini
│   ├── correct2.mini
│   ├── error_undeclared.mini
│   ├── error_redeclare.mini
│   └── error_divzero.mini
└── README.md
```

---

## Example Output

**Correct program:**
```text
[Lexer] Tokens generated successfully.
[Parser] AST created successfully.
[Static Checker] No errors found. Program is valid.
```

**Error program (undeclared variable):**
```text
[Static Checker] Found errors:
  Error at line 3: Variable 'y' used before declaration
```

---

## Concepts Covered

| Component       | Related Area                  |
|----------------|-------------------------------|
| Lexer          | Compilers / Programming Languages |
| Parser + AST   | Compilers / Programming Languages |
| Static Checker | Formal Methods / Program Analysis |
| Interpreter    | Programming Languages         |

---

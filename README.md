Mini Language + Static CheckerThis is a small project where I built a tiny programming language from scratch. The language supports variable declarations, assignments, basic arithmetic, and print statements.The project includes:
A Lexer that breaks the code into tokens
A Parser that builds an Abstract Syntax Tree (AST)
A Static Checker that finds common errors before running the program
An optional Interpreter that can execute the code
I made this project to understand the basic working of compilers and the idea of static analysis (which is related to formal methods).Language FeaturesYou can write simple programs like this:

var x;
var y;
x = 10;
y = x + 5 * 2;
print y;Supported operators: +, -, *, /

Parentheses are also supported.
What the Static Checker Can Detect
Using a variable before declaring it
Declaring the same variable more than once
Division by zero (when dividing by a constant 0)


# Check and run the program
python main.py examples/correct1.mini
python main.py examples/correct1.mini --run

# Structure of the project
├── main.py
├── lexer.py
├── parser.py
├── ast_nodes.py
├── checker.py
├── interpreter.py
├── examples/
│   ├── correct1.mini
│   ├── correct2.mini
│   ├── error_undeclared.mini
│   ├── error_redeclare.mini
│   └── error_divzero.mini
└── README.md
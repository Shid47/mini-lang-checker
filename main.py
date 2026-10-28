
import sys
from lexer import tokenize
from parser import Parser
from checker import StaticChecker
from interpreter import Interpreter


def run_file(filename, execute=False):
    print(f"\n=== Processing: {filename} ===\n")

    try:
        with open(filename, 'r') as f:
            code = f.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return

    print("Source code:")
    print("-" * 40)
    print(code)
    print("-" * 40)

    # 1. Lexing
    try:
        tokens = tokenize(code)
        print("\n[Lexer] Tokens generated successfully.")
    except RuntimeError as e:
        print(f"\n[Lexer Error] {e}")
        return

    # 2. Parsing
    try:
        parser = Parser(tokens)
        ast = parser.parse()
        print("[Parser] AST created successfully.")
    except SyntaxError as e:
        print(f"\n[Parser Error] {e}")
        return

    # 3. Static Checking
    checker = StaticChecker()
    errors = checker.check(ast)

    if errors:
        print("\n[Static Checker] Found errors:")
        for err in errors:
            print("  " + err)
        print("\nProgram rejected.")
        return
    else:
        print("[Static Checker] No errors found. Program is valid.")

    # 4. Optional Execution
    if execute:
        print("\n[Interpreter] Running program...\n")
        try:
            interpreter = Interpreter()
            interpreter.eval(ast)
        except Exception as e:
            print(f"[Runtime Error] {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py <file.mini>           # only check")
        print("  python main.py <file.mini> --run     # check + execute")
        print("\nExample:")
        print("  python main.py examples/correct1.mini --run")
        return

    filename = sys.argv[1]
    execute = '--run' in sys.argv

    run_file(filename, execute=execute)


if __name__ == '__main__':
    main()

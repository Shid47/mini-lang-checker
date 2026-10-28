# Static Checker / Simple Verifier for the Mini Language

from ast_nodes import *


class StaticChecker:
    def __init__(self):
        self.declared = set()      # variables that have been declared
        self.errors = []           # list of error messages

    def check(self, node):
        """Entry point. Returns list of error messages (empty if no errors)."""
        self.declared.clear()
        self.errors.clear()
        self.visit(node)
        return self.errors

    def error(self, message, line):
        self.errors.append(f"Error at line {line}: {message}")

    def visit(self, node):
        if isinstance(node, Program):
            for stmt in node.statements:
                self.visit(stmt)

        elif isinstance(node, VarDecl):
            if node.name in self.declared:
                self.error(f"Variable '{node.name}' is already declared", node.line)
            else:
                self.declared.add(node.name)

        elif isinstance(node, Assign):
            # Check the expression first
            self.visit(node.expr)
            # Variable must be declared before assignment
            if node.name not in self.declared:
                self.error(f"Variable '{node.name}' used before declaration", node.line)

        elif isinstance(node, Print):
            self.visit(node.expr)

        elif isinstance(node, BinOp):
            self.visit(node.left)
            self.visit(node.right)

            # Simple constant division by zero check
            if node.op == '/' and isinstance(node.right, Number) and node.right.value == 0:
                self.error("Division by zero", node.line)

        elif isinstance(node, Variable):
            if node.name not in self.declared:
                self.error(f"Variable '{node.name}' used before declaration", node.line)

        elif isinstance(node, Number):
            pass  # nothing to check

        else:
            raise Exception(f"Unknown AST node: {type(node)}")

# Simple Interpreter (optional - runs the program after checking)

from ast_nodes import *


class Interpreter:
    def __init__(self):
        self.env = {}  # variable name -> value

    def eval(self, node):
        if isinstance(node, Program):
            for stmt in node.statements:
                self.eval(stmt)

        elif isinstance(node, VarDecl):
            self.env[node.name] = 0  # default value

        elif isinstance(node, Assign):
            value = self.eval(node.expr)
            self.env[node.name] = value

        elif isinstance(node, Print):
            value = self.eval(node.expr)
            print(value)

        elif isinstance(node, BinOp):
            left = self.eval(node.left)
            right = self.eval(node.right)
            if node.op == '+':
                return left + right
            elif node.op == '-':
                return left - right
            elif node.op == '*':
                return left * right
            elif node.op == '/':
                if right == 0:
                    raise RuntimeError("Division by zero at runtime")
                return left // right  # integer division

        elif isinstance(node, Number):
            return node.value

        elif isinstance(node, Variable):
            return self.env[node.name]

        else:
            raise Exception(f"Unknown node type: {type(node)}")

# AST Node classes for the Mini Language

class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements  # list of statements

class VarDecl(ASTNode):
    def __init__(self, name, line):
        self.name = name
        self.line = line

class Assign(ASTNode):
    def __init__(self, name, expr, line):
        self.name = name
        self.expr = expr
        self.line = line

class Print(ASTNode):
    def __init__(self, expr, line):
        self.expr = expr
        self.line = line

class BinOp(ASTNode):
    def __init__(self, op, left, right, line):
        self.op = op          # '+', '-', '*', '/'
        self.left = left
        self.right = right
        self.line = line

class Number(ASTNode):
    def __init__(self, value, line):
        self.value = value
        self.line = line

class Variable(ASTNode):
    def __init__(self, name, line):
        self.name = name
        self.line = line

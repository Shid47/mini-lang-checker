# Parser for the Mini Language (Recursive Descent)

from ast_nodes import *


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def eat(self, expected_type):
        token = self.current()
        if token[0] == expected_type:
            self.pos += 1
            return token
        else:
            raise SyntaxError(
                f'Expected {expected_type} but got {token[0]} ({token[1]!r}) at line {token[2]}'
            )

    def parse(self):
        statements = []
        while self.current()[0] != 'EOF':
            statements.append(self.statement())
        return Program(statements)

    def statement(self):
        token = self.current()

        if token[0] == 'VAR':
            return self.var_decl()
        elif token[0] == 'PRINT':
            return self.print_stmt()
        elif token[0] == 'ID':
            return self.assignment()
        else:
            raise SyntaxError(f'Unexpected token {token[0]} at line {token[2]}')

    def var_decl(self):
        self.eat('VAR')
        name_token = self.eat('ID')
        self.eat('SEMI')
        return VarDecl(name_token[1], name_token[2])

    def assignment(self):
        name_token = self.eat('ID')
        self.eat('ASSIGN')
        expr = self.expression()
        self.eat('SEMI')
        return Assign(name_token[1], expr, name_token[2])

    def print_stmt(self):
        print_token = self.eat('PRINT')
        expr = self.expression()
        self.eat('SEMI')
        return Print(expr, print_token[2])

    # Expression parsing with operator precedence
    # expression -> term ( (+|-) term )*
    def expression(self):
        node = self.term()

        while self.current()[0] in ('PLUS', 'MINUS'):
            op_token = self.current()
            self.pos += 1
            right = self.term()
            node = BinOp(op_token[1], node, right, op_token[2])

        return node

    # term -> factor ( (*|/) factor )*
    def term(self):
        node = self.factor()

        while self.current()[0] in ('MUL', 'DIV'):
            op_token = self.current()
            self.pos += 1
            right = self.factor()
            node = BinOp(op_token[1], node, right, op_token[2])

        return node

    # factor -> NUMBER | ID | ( expression )
    def factor(self):
        token = self.current()

        if token[0] == 'NUMBER':
            self.pos += 1
            return Number(int(token[1]), token[2])
        elif token[0] == 'ID':
            self.pos += 1
            return Variable(token[1], token[2])
        elif token[0] == 'LPAREN':
            self.eat('LPAREN')
            node = self.expression()
            self.eat('RPAREN')
            return node
        else:
            raise SyntaxError(f'Unexpected token {token[0]} in expression at line {token[2]}')

# Lexer (Tokenizer) for the Mini Language

import re

# Token types
TOKEN_TYPES = [
    ('VAR',      r'\bvar\b'),
    ('PRINT',    r'\bprint\b'),
    ('NUMBER',   r'\d+'),
    ('ID',       r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('ASSIGN',   r'='),
    ('PLUS',     r'\+'),
    ('MINUS',    r'-'),
    ('MUL',      r'\*'),
    ('DIV',      r'/'),
    ('SEMI',     r';'),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('SKIP',     r'[ \t]+'),
    ('NEWLINE',  r'\n'),
    ('MISMATCH', r'.'),
]

# Build the master regex
master_pattern = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES)
regex = re.compile(master_pattern)


def tokenize(code):
    """
    Convert source code into a list of tokens.
    Each token is a tuple: (type, value, line_number)
    """
    tokens = []
    line_num = 1

    for match in regex.finditer(code):
        kind = match.lastgroup
        value = match.group()

        if kind == 'NEWLINE':
            line_num += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value!r} at line {line_num}')
        else:
            tokens.append((kind, value, line_num))

    tokens.append(('EOF', '', line_num))  # End of file marker
    return tokens

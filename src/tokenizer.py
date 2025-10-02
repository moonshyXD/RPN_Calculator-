from typing import List
from .numbers import to_number


def tokenize(expression: str) -> List[str]:
    """
    Tokenize an RPN expression line.
    Assumes tokens are separated by whitespace.
    Numbers may have leading + or -.
    """
    raw_tokens = expression.strip().split()
    tokens = []
    for p in raw_tokens:
        if p == '' or p is None:
            continue
        if p in ("(", ")"):
            tokens.append(p)
        if p[0] == "~":
            tokens.append(str(-to_number(p[1:])))
        elif p[0] == "$":
            tokens.append(p[1:])
        else:
            tokens.append(p)
    return tokens

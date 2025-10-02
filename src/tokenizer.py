import re
from typing import List
from .numbers import to_number


def tokenize(expression: str) -> List[str]:
    """
    Tokenize an RPN expression line.
    Assumes tokens are separated by whitespace.
    Numbers may have leading + or -.
    """
    regular_verb = r"[()]|[~$]?\d+(?:\.\d+)?(?:e[+-]?\d+)?|[+\-*/%]+"
    raw_tokens = re.findall(regular_verb, expression)

    tokens = []
    for t in raw_tokens:
        if t.startswith("~"):
            tokens.append(str(-to_number(t[1:])))
        elif t.startswith("$"):
            tokens.append(t[1:])
        else:
            tokens.append(t)

    return tokens

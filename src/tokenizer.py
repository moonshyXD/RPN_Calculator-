from typing import List
from .numbers import to_number


def handle_unary_minus(token: str) -> str:
    """
    Process a token with one or multiple '~' prefixes representing unary minus.
    :param token: The token starting with '~'.
    :return: String result with precessed unary minus.
    """
    count_minus = 0
    result: str
    for i in range(len(token)):
        if token[i] == "~":
            count_minus += 1
        else:
            result = str(to_number(token[i:]))
            if count_minus % 2 != 0:
                result = "-" + result

    return result


def tokenize(expression: str) -> List[str]:
    """
    Tokenize an RPN expression line into a list of tokens.
    Handles special cases like negative numbers with '~' prefix
    and variables with '$' prefix.

    :param expression: The RPN expression.
    :return: List of the tokens.
    """
    raw_tokens = expression.strip().split()
    tokens = []
    for token in raw_tokens:
        if token == '' or token is None:
            continue
        if token in ("(", ")"):
            tokens.append(token)
        if token[0] == "~":
            to_append = handle_unary_minus(token)
            tokens.append(to_append)
        elif token[0] == "$":
            tokens.append(token[1:])
        else:
            tokens.append(token)
    return tokens

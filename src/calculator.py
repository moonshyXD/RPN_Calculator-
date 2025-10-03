from typing import List, Union
from .numbers import to_number, is_number
from .operations import OPERATORS
from .calculator_errors import CalculatorSyntaxError

Number = Union[int, float]


def _push(stack: List[List[Number]], value: Number) -> None:
    """
    Push a value onto the top stack.

    :param stack: The stack of number lists.
    :param value: The number value to push.
    """
    stack[-1].append(value)


def _pop(stack: List[List[Number]]) -> Number:
    """
    Pop a value from the top stack.

    :param stack: The stack of number lists.
    :return: The popped number value.
    :raises CalculatorSyntaxError: If top stack is empty.
    """
    if not stack[-1]:
        raise CalculatorSyntaxError("Not enough values for operation")
    return stack[-1].pop()


def _handle_parentheses(stack: List[List[Number]], token: str) -> None:
    """
    Handle parentheses tokens in the expression.

    :param stack: The stack of number lists.
    :param token: The parenthesis token ("(" or ")").
    :raises CalculatorSyntaxError: For unbalanced parentheses or
    closed parentheses without open.
    """
    if token == "(":
        stack.append([])
    elif token == ")":
        if len(stack) == 1:
            raise CalculatorSyntaxError("Closed parenthesis without open")
        inner = stack.pop()
        if len(inner) != 1:
            raise CalculatorSyntaxError(
                "Parenthesis content must reduce to single value"
            )
        _push(stack, inner[0])


def calculate(tokens: List[str]) -> Number:
    """
    Evaluate tokens in RPN notation.

    :param tokens: List of tokens from tokenized RPN expression.
    :return: The calculated result as int or float.
    :raises CalculatorSyntaxError: For syntax errors, unknown tokens,
    unbalanced parentheses, or invalid expressions.
    """
    stack: List[List[Number]] = [[]]

    for token in tokens:
        if token in ("(", ")"):
            _handle_parentheses(stack, token)
            continue

        if is_number(token):
            _push(stack, to_number(token))
            continue

        if token not in OPERATORS:
            raise CalculatorSyntaxError(f"Unknown token: {token}")

        if len(stack[-1]) < 2:
            raise CalculatorSyntaxError(f"Not enough operands for {token}")

        b = _pop(stack)
        a = _pop(stack)
        result = OPERATORS[token](a, b)
        _push(stack, result)

    if len(stack) != 1:
        raise CalculatorSyntaxError("Unbalanced parentheses")

    output = stack[0]
    if len(output) != 1:
        raise CalculatorSyntaxError("Invalid RPN expression")
    return output[0]

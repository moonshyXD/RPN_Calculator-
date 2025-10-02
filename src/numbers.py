from typing import Union, Optional
from .calculator_errors import CalculatorSyntaxError

Number = Union[int, float]


def parse_number(token: str) -> Optional[Number]:
    """
    Parse token into int or float if possible, else return None.

    :param token: The string token to parse.
    :return: int or float if valid number, else None.
    """
    try:
        if "." in token or "e" in token or "E" in token:
            num = float(token)
            return int(num) if num.is_integer() else num
        return int(token)
    except ValueError:
        return None


def to_number(token: str) -> Number:
    """
    Convert token to number or raise CalculatorSyntaxError.

    :param token: The string token to convert.
    :return: int or float.
    :raises CalculatorSyntaxError: if token is invalid.
    """
    value = parse_number(token)
    if value is None:
        raise CalculatorSyntaxError(f"Invalid number: {token}")
    return value


def is_number(token: str) -> bool:
    """
    Check if token is a number.

    :param token: The string token to check.
    :return: True if valid number, False otherwise.
    """
    return parse_number(token) is not None

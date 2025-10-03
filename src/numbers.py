from typing import Union, Optional
from .calculator_errors import CalculatorSyntaxError

Number = Union[int, float]


def parse_number(token: str) -> Optional[Number]:
    """
    Преобразовать str токен в int или float, если это возможно.

    :param token: str токен.
    :return: int или float, если число корректное, иначе None.
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
    Преобразовать str токен в число или вызвать ошибку.

    :param token: str токен.
    :return: int или float.
    :raises CalculatorSyntaxError: Если токен не является числом.
    """
    value = parse_number(token)
    if value is None:
        raise CalculatorSyntaxError(f"Некорректное число: {token}")
    return value


def is_number(token: str) -> bool:
    """
    Проверить, является ли токен числом.

    :param token: str токен.
    :return: True, если число корректное, иначе False.
    """
    return parse_number(token) is not None

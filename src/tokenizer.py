from typing import List
from .numbers import to_number
from .calculator_errors import CalculatorSyntaxError


def handle_unary_minus(token: str) -> str:
    """
    Обработать токен с одним или несколькими префиксами '~' (унарный минус).

    :param token: Токен, начинающийся с '~'.
    :return: Строковое представление обработанного числа.
    :raises CalculatorSyntaxError: Если токен некорректный.
    """
    count_minus: int = 0
    result: str = ""
    for i in range(len(token)):
        if token[i] == "~":
            count_minus += 1
        else:
            result = str(to_number(token[i:]))
            if count_minus % 2 != 0:
                result = "-" + result
            break

    if not any(elem.isdigit() for elem in result):
        raise CalculatorSyntaxError(f"Неизвестный токен: {token}")
    return result


def handle_unary_plus(token: str) -> str:
    """
    Обработать токен с префиксом '$' (унарный плюс).

    :param token: Токен, начинающийся с '$'.
    :return: Строковое представление числа.
    :raises CalculatorSyntaxError: Если токен некорректный.
    """
    result: str = str(to_number(token[1:]))

    if not any(elem.isdigit() for elem in result):
        raise CalculatorSyntaxError(f"Неизвестный токен: {token}")
    return result


def tokenize(expression: str) -> List[str]:
    """
    Разбить строку выражения RPN на список токенов.
    Обрабатывает:
      - скобки
      - отрицательные числа с префиксом '~'
      - положительные числа с префиксом '$'
      - обычные числа и операторы

    :param expression: Строка выражения RPN.
    :return: Список токенов.
    """
    raw_tokens = expression.strip().split()
    tokens: List[str] = []
    for token in raw_tokens:
        if token == '' or token is None:
            continue
        if token in ("(", ")"):
            tokens.append(token)
        elif token[0] == "~":
            to_append = handle_unary_minus(token)
            tokens.append(to_append)
        elif token[0] == "$":
            to_append = handle_unary_plus(token)
            tokens.append(to_append)
        else:
            tokens.append(token)
    return tokens

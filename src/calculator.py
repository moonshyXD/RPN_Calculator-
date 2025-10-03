from typing import List, Union
from .numbers import to_number, is_number
from .operations import OPERATORS
from .calculator_errors import CalculatorSyntaxError

Number = Union[int, float]


def _push(stack: List[List[Number]], value: Number) -> None:
    """
    Добавить число в верхний стек.

    :param stack: Стек, состоящий из списков чисел.
    :param value: Число для добавления.
    """
    stack[-1].append(value)


def _pop(stack: List[List[Number]]) -> Number:
    """
    Извлечь число из верхнего стека.

    :param stack: Стек, состоящий из списков чисел.
    :return: Извлечённое число.
    :raises CalculatorSyntaxError: Если верхний стек пуст.
    """
    if not stack[-1]:
        raise CalculatorSyntaxError("Недостаточно значений для операции")
    return stack[-1].pop()


def _handle_parentheses(stack: List[List[Number]], token: str) -> None:
    """
    Обработка токенов скобок в выражении.

    :param stack: Стек, состоящий из списков чисел.
    :param token: Токен скобки '(' или ')'.
    :raises CalculatorSyntaxError: При несбалансированных скобках или
    закрывающей скобке без открывающей.
    """
    if token == "(":
        stack.append([])
    elif token == ")":
        if len(stack) == 1:
            raise CalculatorSyntaxError("Закрывающая скобка без открывающей")
        inner = stack.pop()
        if len(inner) != 1:
            raise CalculatorSyntaxError(
                "Содержимое скобок должно сводиться к одному значению"
            )
        _push(stack, inner[0])


def calculate(tokens: List[str]) -> Number:
    """
    Вычислить выражение в обратной польской нотации (RPN).

    :param tokens: Список токенов (результат токенизации выражения).
    :return: Результат вычисления (int или float).
    :raises CalculatorSyntaxError: При синтаксических ошибках,
    неизвестных токенах, несбалансированных скобках или неверных выражениях.
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
            raise CalculatorSyntaxError(f"Неизвестный токен: {token}")

        if len(stack[-1]) < 2:
            raise CalculatorSyntaxError(f"Недостаточно операндов для {token}")

        b = _pop(stack)
        a = _pop(stack)
        result = OPERATORS[token](a, b)
        _push(stack, result)

    if len(stack) != 1:
        raise CalculatorSyntaxError("Несбалансированные скобки")

    output = stack[0]
    if len(output) != 1:
        raise CalculatorSyntaxError("Некорректное выражение RPN")
    return output[0]

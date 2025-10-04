from typing import List, Union
from src.numbers import to_number, is_number
from src.operations import OPERATORS
from src.calculator_errors import CalculatorSyntaxError

Number = Union[int, float]


def push_value(stack: List[List[Number]], value: Number) -> None:
    """
    Добавить число в верхний стек.

    :param stack: Стек, состоящий из списков чисел.
    :param value: Число для добавления.
    """
    stack[-1].append(value)


def pop_value(stack: List[List[Number]]) -> Number:
    """
    Извлечь число из верхнего стека.

    :param stack: Стек, состоящий из списков чисел.
    :return: Извлечённое число.
    :raises CalculatorSyntaxError: Если верхний стек пуст.
    """
    if not stack[-1]:
        raise CalculatorSyntaxError("Недостаточно значений для операции")
    return stack[-1].pop()


def handle_parentheses(stack: List[List[Number]], token: str) -> None:
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
        push_value(stack, inner[0])


def calculate(tokens: List[str]) -> Number:
    """
    Вычислить выражение в обратной польской нотации (RPN).

    :param tokens: Список токенов (результат токенизации выражения).
    :return: Результат вычисления (int или float).
    :raises CalculatorSyntaxError: При синтаксических ошибках,
    неизвестных токенах, несбалансированных скобках или неверных выражениях.
    """
    stack: List[List[Number]] = [[]]

    for current_token in tokens:
        if current_token in ("(", ")"):
            handle_parentheses(stack, current_token)
            continue

        if is_number(current_token):
            push_value(stack, to_number(current_token))
            continue

        if current_token not in OPERATORS:
            raise CalculatorSyntaxError(f"Неизвестный токен: {current_token}")

        if len(stack[-1]) < 2:
            raise CalculatorSyntaxError(
                f"Недостаточно операндов для {current_token}"
                )

        b = pop_value(stack)
        a = pop_value(stack)
        result = OPERATORS[current_token](a, b)
        push_value(stack, result)

    if len(stack) != 1:
        raise CalculatorSyntaxError("Несбалансированные скобки")

    output = stack[0]
    if len(output) != 1:
        raise CalculatorSyntaxError("Некорректное выражение RPN")
    return output[0]

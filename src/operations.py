from src.numbers import Number
from src.calculator_errors import CalculatorTypeError, \
    CalculatorZeroDivisionError
from src.constants import MAX_POWER


def division(a: Number, b: Number) -> Number:
    """
    Деление с проверкой деления на ноль.

    :param a: Делимое (int или float).
    :param b: Делитель (int или float).
    :return: Результат деления (int, если результат целый, иначе float).
    :raises CalculatorZeroDivisionError: Если делитель равен нулю.
    """
    if b == 0:
        raise CalculatorZeroDivisionError("Деление на ноль (float)")
    result = a / b
    return int(result) if result.is_integer() else result


def int_division(a: Number, b: Number) -> int:
    """
    Целочисленное деление с проверкой типов и деления на ноль.

    :param a: Делимое (только int).
    :param b: Делитель (только int).
    :return: Результат целочисленного деления.
    :raises CalculatorTypeError: Если хотя бы один операнд не int.
    :raises CalculatorZeroDivisionError: Если делитель равен нулю.
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        raise CalculatorTypeError("// работает только с целыми числами")
    if b == 0:
        raise CalculatorZeroDivisionError("Целочисленное деление на ноль")
    return a // b


def modulo(a: Number, b: Number) -> int:
    """
    Операция взятия остатка от деления с проверкой типов и нуля.

    :param a: Делимое (только int).
    :param b: Делитель (только int).
    :return: Остаток от деления.
    :raises CalculatorTypeError: Если хотя бы один операнд не int.
    :raises CalculatorZeroDivisionError: Если делитель равен нулю.
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        raise CalculatorTypeError("% работает только с целыми числами")
    if b == 0:
        raise CalculatorZeroDivisionError("Остаток от деления на ноль")
    return a % b


OPERATORS = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': division,
    '//': int_division,
    '%': modulo,
    '**': lambda a, b: a ** b if abs(b) < MAX_POWER else float('inf')
}

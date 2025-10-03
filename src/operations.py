from .numbers import Number
from .calculator_errors import CalculatorTypeError, CalculatorZeroDivisionError
from .constants import MAX_POWER


def division(a: Number, b: Number) -> Number:
    """
    Perform division with zero check and integer conversion.

    :param a: Dividend (int or float)
    :param b: Divisor (int or float)
    :return: Division result as int if integer, else float
    :raises CalculatorZeroDivisionError: If divisor is zero
    """
    if b == 0:
        raise CalculatorZeroDivisionError("Float division by zero")
    result = a / b
    return int(result) if result.is_integer() else result


def int_division(a: Number, b: Number) -> int:
    """
    Perform integer division with type and zero checks.

    :param a: Dividend (must be int)
    :param b: Divisor (must be int)
    :return: Integer division result
    :raises CalculatorTypeError: If operands are not integers
    :raises CalculatorZeroDivisionError: If divisor is zero
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        raise CalculatorTypeError("// works only with integers")
    if b == 0:
        raise CalculatorZeroDivisionError("Integer division by zero")
    return a // b


def modulo(a: Number, b: Number) -> int:
    """
    Perform modulo operation with type and zero checks.

    :param a: Dividend (must be int)
    :param b: Divisor (must be int)
    :return: Modulo operation result
    :raises CalculatorTypeError: If operands are not integers
    :raises CalculatorZeroDivisionError: If divisor is zero
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        raise CalculatorTypeError("% works only with integers")
    if b == 0:
        raise CalculatorZeroDivisionError("Integer modulo by zero")
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

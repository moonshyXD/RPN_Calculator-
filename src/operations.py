from .calculator_errors import CalculatorTypeError, CalculatorZeroDivisionError
from .constants import MAX_POWER


def division(a, b):
    if b == 0:
        raise CalculatorZeroDivisionError("Float division by zero")
    result = a / b
    return int(result) if result.is_integer() else result


def int_division(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise CalculatorTypeError("// works only with integers")
    if b == 0:
        raise CalculatorZeroDivisionError("Integer division by zero")
    return a // b


def modulo(a, b):
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

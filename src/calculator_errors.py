class CalculatorError(Exception):
    """Базовое исключение калькулятора"""
    pass


class CalculatorZeroDivisionError(CalculatorError, ZeroDivisionError):
    """Деление на ноль в калькуляторе"""
    pass


class CalculatorTypeError(CalculatorError, TypeError):
    """Неверные типы операндов в калькуляторе"""
    pass


class CalculatorSyntaxError(CalculatorError, SyntaxError):
    """Синтаксическая ошибка в выражении калькулятора"""
    pass

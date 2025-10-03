import sys
from .tokenizer import tokenize
from .calculator import calculate
from .calculator_errors import CalculatorError


def run() -> None:
    """
    Запуск калькулятора RPN.
    Считывает выражения из стандартного ввода,
    токенизирует и вычисляет их,
    обрабатывает различные ошибки калькулятора.
    """
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            tokens = tokenize(line)
            result = calculate(tokens)
            print(result)
        except ValueError:
            print("inf")
        except CalculatorError as e:
            print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    run()

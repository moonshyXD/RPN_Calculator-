import sys
from .tokenizer import tokenize
from .calculator import calculate
from .calculator_errors import CalculatorError


def run() -> None:
    """
    Run the RPN calculator interactive session.
    Reads expressions from standard input, tokenizes and calculates them,
    handling various calculator errors appropriately.
    """
    print(
        "Welcome to RPN calculator! Enter RPN expressions, "
        "tokens separated by spaces. "
        "Parentheses allowed. "
        "Unary +-($~) must be written with number without space."
    )
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
            print("CalculatorError:", e)


if __name__ == "__main__":
    run()

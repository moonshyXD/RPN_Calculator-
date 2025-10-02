import pytest
from src.tokenizer import tokenize
from src.calculator import calculate

tests_simple = [
    ("3 4 +", 7),                       # 3 + 4
    ("10 2 -", 8),                      # 10 - 2
    ("10 2 *", 20),                     # 10 * 2
    ("11 2 /", 5.5),                    # 11 / 2
    ("11 2 //", 5),                     # 11 // 2
    ("11 2 %", 1),                      # 11 % 2
    ("11 2 **", 121),                   # 11 ** 2
    ("3 4 2 * +", 11),                  # 3 + 4 * 2
    ("5 1 2 + 4 * + 3 -", 14),          # 5 + (1 + 2) * 4 - 3
    ("3.5 2 *", 7.0),                   # дробные числа
    ("3", 3),                           # одно число
    ("~3", -3),                         # число с унарным минусом
    ("$3", 3),                          # число с унарным плюсом
    ("1e3 2 +", 1002),                  # число в экспоненциальной форме
    ("2 1e-3 *", 0.002),                # очень маленькое число
    ("3.0 2 +", 5),                     # float, который превращается в int
    ("5 ~3 +", 2),                      # унарный минус внутри выражения
    ("5 $3 +", 8),                      # унарный плюс внутри выражения
    ("2 3 2 ** **", 512),               # проверка степени
    ("0 0 **", 1),                      # 0 ** 0 = 1
    ("( ( 3 ) )", 3),                   # вложенные пустые скобки
    ("2 3 + 4 *", 20),                  # последовательные операции
    ("5 1 2 + 4 ** + 3 -", 83),         # более сложное выражение со степенью
]

tests_zero_division = [
    ("3 0 /", ZeroDivisionError),       # деление на 0
    ("3 0 //", ZeroDivisionError),      # целочисленное деление на 0
    ("3 0 %", ZeroDivisionError),       # остаток от деления на 0
]

tests_type_error = [
    ("3.5 2 //", TypeError),            # float для деления //
    ("3.5 2 %", TypeError),             # float для %
]

tests_large_power = [
    (f"2 {10**9} **", float('inf')),    # слишком большая степень
    ("2 1000000 **", float('inf')),     # граничное значение MAX_POWER
    ("2 -100 **", 7.888609052210118e-31),                 # маленькая степень
]

tests_syntax_error = [
    ("3 +", SyntaxError),               # недостаточно аргументов
    ("3 4 &", SyntaxError),             # неизвестная операция
    ("", SyntaxError),                  # пустое выражение
    ("3 4 + 5", SyntaxError),           # слишком много чисел
    ("abc 2 +", SyntaxError),           # некорректный токен
    ("--3 2 +", SyntaxError),           # двойной минус в числе
    ("+", SyntaxError),                 # оператор без аргументов
]

tests_parentheses_valid = [
    ("( 3 4 + )", 7),                   # скобки вокруг выражения
    ("2 ( 3 4 * ) +", 14),              # вложенные скобки в конце
    ("( 3 4 * ) 2 +", 14),              # вложенные скобки в начале
    ("2 3 + ( 3 4 * ) 3 + +", 20),      # вложенные внутри
]

tests_parentheses_invalid = [
    ("( 3 4 +", SyntaxError),       # открыта без закрытия
    ("3 4 + )", SyntaxError),       # закрыта без открытия
    ("( 2 + 3 ) )", SyntaxError),   # лишняя закрывающая
    ("( ( 2 + 3 )", SyntaxError),   # лишняя открывающая
    (") 2 3 + (", SyntaxError),     # скобки в неправильном порядке
    ("()", SyntaxError),            # пустые скобки
    ("( 2 3 )", SyntaxError),       # внутри несколько чисел, но нет операции
]

correct_tests = tests_simple + tests_large_power + tests_parentheses_valid
incorrect_tests = tests_zero_division + tests_type_error \
      + tests_syntax_error + tests_parentheses_invalid


@pytest.mark.parametrize("expr, expected", correct_tests)
def test_correct(expr, expected):
    tokens = tokenize(expr)
    result = calculate(tokens)
    assert result == expected, f"{expr} -> {result}, expected {expected}"


@pytest.mark.parametrize("expr, expected_exception", incorrect_tests)
def test_exceptions(expr, expected_exception):
    with pytest.raises(expected_exception):
        tokens = tokenize(expr)
        calculate(tokens)

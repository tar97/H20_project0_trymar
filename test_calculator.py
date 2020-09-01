import calculator
import math
import pytest
eps = 1e-12


def test_add_exercise_1():
    a, b = 1, 2
    assert calculator.add(a, b) == 3


def test_add_fl_exercise_2():
    a, b = 0.1, 0.2
    ans = 0.3
    assert abs(calculator.add(a, b) - ans)\
           < eps


def test_add_str_exercise_3():
    w1, w2 = "Hello ", "World"
    sentence = "Hello World"
    assert calculator.add(w1, w2) \
        == sentence


def test_add_typerr_exercise_5():
    with pytest.raises(TypeError):
        calculator.add("hello", 5)


def test_exponential_exercise_4():
    assert calculator.factorial(0) == 1
    x = 10
    ans = 3628800
    assert calculator.factorial(x) \
           == ans


def test_sin_zero_exercise_4():
    acc = 50
    x = 0
    ans = 0
    diff = abs(calculator.sin(x, acc) - ans)
    assert diff < eps


def test_sin_fourth_exercise_4():
    acc = 50
    x = math.pi/4
    ans = math.pow(2, 0.5) / 2
    diff = abs(calculator.sin(x, acc) - ans)
    assert diff < eps


def test_sin_half_exercise_4():
    acc = 50
    x = math.pi / 2
    ans = 1
    diff = abs(calculator.sin(x, acc) - ans)
    assert diff < eps


def test_sin_2quad_exercise_4():
    acc = 50
    x = 5 * math.pi / 6
    ans = 1. / 2
    diff = abs(calculator.sin(x, acc) - ans)
    assert diff < eps


def test_sin_3quad_exercise_4():
    acc = 50
    x = 7 * math.pi / 6
    ans = - 1.0 / 2
    diff = abs(calculator.sin(x, acc) - ans)
    assert diff < eps


def test_sin_4quad_exercise_4():
    acc = 50
    x = 7 * math.pi / 4
    ans = - math.pow(2, 0.5) / 2
    diff = abs(calculator.sin(x, acc) - ans)
    assert diff < eps


def test_divide_zero_exercise_4():
    x, y = 0, 5
    assert calculator.divide(x, y) \
        == 0


def test_divide_one_exercise_4():
    x, y = 10, 1
    assert calculator.divide(x, y) \
        == x


def test_divide_exercise_4():
    x, y = 15, 5
    assert calculator.divide(x, y) \
        == 3


def test_divide_frac_exercise_4():
    x, y = 5, 10
    assert abs(calculator.divide(x, y) - 0.5) \
        < eps


def test_divide_zerodiverr_exercise_5():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5, 0)


def test_binomial_zero_exercise_4():
    n, k = 10, 0
    assert abs(calculator.binomial(n, k) - 1) \
        < eps


def test_binomial_exercise_4():
    n, k = 10, 6
    ans = 210
    assert abs(calculator.binomial(n, k) - ans) \
        < eps


def test_signum_neg_exercise_4():
    x = -5
    assert calculator.signum(x) == -1


def test_signum_zero_exercise_4():
    x = 0
    assert calculator.signum(x) == 0


def test_signum_pos_exercise_4():
    x = 6
    assert calculator.signum(x) == 1



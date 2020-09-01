import calculator
import math
import pytest
eps = 1e-12


@pytest.mark.parametrize("arg, exp", [[(1, 2), 3],
                                      [(5, 6), 11],
                                      [(0, 1), 1],
                                      [(-4, 10), 6]])
def test_add_exercise_1(arg, exp):
    assert calculator.add(arg[0], arg[1]) == exp


@pytest.mark.parametrize("arg, exp", [[(1.0, 2.0), 3.0],
                                      [(5.0, 6.0), 11.0],
                                      [(0.0, 1.0), 1.0],
                                      [(-4.0, 10.0), 6.0],
                                      [(0.5, 0.4), 0.9]])
def test_add_fl_exercise_2(arg, exp):
    a, b = arg
    assert abs(calculator.add(a, b) - exp)\
           < eps


@pytest.mark.parametrize("arg, exp", [[("Hello ", "world"), "Hello world"],
                                      [("", "h"), "h"],
                                      [("hey", " "), "hey "]])
def test_add_str_exercise_3(arg, exp):
    w1, w2 = arg
    assert calculator.add(w1, w2) \
        == exp


@pytest.mark.parametrize("arg", [("Hello ", 5),
                                 ("", -8)])
def test_add_typerr_exercise_5(arg):
    with pytest.raises(TypeError):
        calculator.add(arg)


@pytest.mark.parametrize("arg, exp", [(0, 1),
                                      (10, 3628800),
                                      (4, 24)])
def test_exponential_exercise_4(arg, exp):
    assert calculator.factorial(arg) \
           == exp


@pytest.mark.parametrize("arg, exp", [(0, 0),
                                      (math.pi/4, math.pow(2, 0.5) / 2),
                                      (math.pi/2, 1),
                                      (5 * math.pi / 6, 1.0 / 2),
                                      (7 * math.pi / 6, -1.0 / 2),
                                      (7 * math.pi / 4, - math.pow(2, 0.5) / 2),
                                      (2*math.pi, 0)])
def test_sin_exercise_5(arg, exp):
    acc = 50
    diff = abs(calculator.sin(arg, acc) - exp)
    assert diff < eps


@pytest.mark.parametrize("args, exp", [[(0, 5), 0],
                                        [(10, 1), 10],
                                       [(15, 5), 3],
                                       [(5, 10), 0.5]])
def test_divide_zero_exercise_5(args, exp):
    x, y = args
    assert calculator.divide(x, y) \
        == exp


def test_divide_zerodiverr_exercise_5():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5, 0)


@pytest.mark.parametrize("args, exp", [[(10, 0), 1],
                                       [(10, 6), 210]])
def test_binomial_exercise_5(args, exp):
    n, k = args
    assert abs(calculator.binomial(n, k) - exp) \
        < eps


@pytest.mark.parametrize("arg, exp", [(-5, -1),
                                      (0, 0),
                                      (5, 1)])
def test_signum_exercise_5(arg, exp):
    assert calculator.signum(arg) == exp

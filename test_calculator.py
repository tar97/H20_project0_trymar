import calculator


def test_add_exercise_1():
    a, b = 1, 2
    assert calculator.add(a, b) == 3


def test_add_fl_exercise_2():
    a, b = 0.1, 0.2
    ans = 0.3
    eps = 1e-12
    assert abs(calculator.add(a, b) - ans)\
           < eps


def test_add_str_exercise_3():
    w1, w2 = "Hello ", "World"
    sentence = "Hello World"
    assert calculator.add(w1, w2) \
        == sentence

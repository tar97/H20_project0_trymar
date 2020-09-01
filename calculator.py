def add(x, y):
    return x + y


def factorial(n):
    k = n
    res = 1
    while k > 0:
        res *= k
        k -= 1
    return res


def sin(x, n):
    res = 0
    for i in range(n+1):
        num = (-1)**i * x**(2*i + 1)
        denom = factorial(2*i + 1)
        res += num / denom
    return res


def divide(x, y):
    return float(x) / y


def binomial(n, k):
    num = factorial(n)
    denom = factorial(k) * factorial(n - k)
    return num / denom


def signum(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1

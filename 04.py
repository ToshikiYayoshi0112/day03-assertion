#  2つの整数の割り算関数div ただし小数点第一位までにすること


def div(x, y):
    return round(x / y, 1)


assert 5.0 == div(10, 2)

assert 3.3 == div(10, 3)


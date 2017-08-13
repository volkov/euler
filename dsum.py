def dsum(x):
    dsum = 0
    while x > 0:
        dsum += x % 10
        x = x // 10
    return dsum


def digits(x):
    while x > 0:
        yield x % 10
        x //= 10

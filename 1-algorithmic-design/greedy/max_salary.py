# Uses python3

import sys


def largest_number(a: list[str]):
    res = ""
    while len(a) > 0:
        max = a[0]
        for x in a:
            if is_greater_or_equal(x, max):
                max = x
        res += max
        a.remove(max)
    return res


def is_greater_or_equal(x, y):
    if x + y >= y + x:
        return True
    return False


if __name__ == "__main__":
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))

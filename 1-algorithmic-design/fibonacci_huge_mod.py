# Uses python3
import sys


def fibonacci_huge_mod(n, m):
    period = pisano_period(m)
    n = n % period
    fibonacci = calc_fib(n)
    return fibonacci % m


def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


def calc_fib(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


if __name__ == "__main__":
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(fibonacci_huge_mod(n, m))

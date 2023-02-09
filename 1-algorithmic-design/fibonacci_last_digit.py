# Uses python3
def calc_fib_last_digit(n):
    if n <= 1:
        return n
    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current


n = int(input())
print(calc_fib_last_digit(n))

# Uses python3
def calc_fib_last_digit(n):
    fib_dict = {0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8}
    if n in fib_dict:
        return fib_dict[n]
    previous, current = 5, 8
    for _ in range(5, n - 1):
        previous, current = current, (previous + current) % 10

    return current


n = int(input())
print(calc_fib_last_digit(n))

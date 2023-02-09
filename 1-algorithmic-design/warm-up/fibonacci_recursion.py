def fibonacci_recursion_naive(num):
    if num <= 1:
        return num
    else:
        return fibonacci_recursion_naive(num - 2) + fibonacci_recursion_naive(num - 1)


def fibonnaci_recursion_memoized(n):
    def fib_memo(n, m):
        if n in m:
            return m[n]

        answer = fib_memo(n - 1, m) + fib_memo(n - 2, m)
        m[n] = answer
        return answer

    m = {1: 1, 2: 1}
    return fib_memo(n, m)


if __name__ == "__main__":
    print(fibonacci_recursion_naive(10))
    print(fibonnaci_recursion_memoized(10))

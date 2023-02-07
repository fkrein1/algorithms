def fibonacci_naive(num):
    if num <= 1:
        return num
    else:
        return fibonacci_naive(num - 2) + fibonacci_naive(num - 1)


def fibonnaci_optmized(num):
    list = [0, 1]
    for i in range(2, num + 1):
        list.append(list[i - 1] + list[i - 2])
    return list[-1]


def fibonnaci_memoized(n):
    def fib_memo(n, m):
        if n in m:
            return m[n]

        answer = fib_memo(n - 1, m) + fib_memo(n - 2, m)
        m[n] = answer
        return answer

    m = {1: 1, 2: 1}
    return fib_memo(n, m)


if __name__ == "__main__":
    print(fibonacci_naive(10))
    print(fibonnaci_optmized(10))


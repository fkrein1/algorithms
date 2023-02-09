# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0
    items = []

    for i in range(len(weights)):
        items.append((values[i] / weights[i], weights[i]))

    items.sort(reverse=True)

    for item in items:
        if capacity > item[1]:
            value += item[1] * item[0]
            capacity -= item[1]
        else:
            value += item[0] * capacity
            return value

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

# Uses python3
import sys

# last digit of sum
def fibonacci_partial_sum(from_, to):
    sum = 0

    to = to % 60
    from_ = from_ % 60

    if to < from_:
        from_ += 60

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


if __name__ == "__main__":
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))

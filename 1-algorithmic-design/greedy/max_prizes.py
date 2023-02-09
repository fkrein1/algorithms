# Uses python3
import sys


def optimal_summands(n):
    if n <= 2:
        return [n]

    summands = []
    itens = n
    for i in range(1, n):
        if i > itens:
            summands[-1] += itens
            break
        else:
            summands.append(i)
            itens -= i

    return summands


if __name__ == "__main__":
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=" ")

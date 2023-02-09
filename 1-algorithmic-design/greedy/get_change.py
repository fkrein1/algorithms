# Uses python3
import sys


def get_change(m):
    coins = 0
    coins += m // 10
    m = m % 10

    coins += m // 5
    m = m % 5

    coins += m // 1
    m = m % 1

    return coins


if __name__ == "__main__":
    m = int(sys.stdin.read())
    print(get_change(m))

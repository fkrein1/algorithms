# Uses python3
import sys


def get_majority_element(a):
    a.sort()
    majority = len(a) / 2
    count = 1
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            count += 1
        else:
            count = 1
        if count > majority:
            return 1
    return 0


def get_majority_element_optimal(a):
    majority = len(a) / 2
    letters = {}
    for i in a:
        try:
            letters[i] += 1
        except:
            letters[i] = 1
    for letter in letters:
        print(letter)
        if letters[letter] > majority:
            return 1
    return 0


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element_optimal(a))

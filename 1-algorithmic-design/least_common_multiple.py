def lcm(a, b):
    return (a * b) // gcd(a, b)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    print(lcm(3918848, 1653264))

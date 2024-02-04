"""
2.1.8 Least Common Multiple

Compute the least common multiple of two pos- itive integers.

Input: Two positive integers a and b.
Output: The least common mul- tiple of a and b.

"""


def gcd(a: int, b: int) -> int:
    if a < b:
        a, b = b, a

    gcd = 1
    while a & 1 == 0 and b & 1 == 0:
        gcd = gcd << 1
        a = a >> 1
        b = b >> 1

    while a & 1 == 0:
        a = a >> 1
    while b & 1 == 0:
        b = b

    while b != 0:
        a = a - b
        while a & 1 == 0 and a > 0:
            a = a >> 1
        if a < b:
            a, b = b, a

    return a * gcd


def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    if b == 1:
        return a
    return (a * b) // gcd(a, b)


def test():
    result = lcm(761457, 614573)
    print(result)
    assert 467970912861 == result


if __name__ == "__main__":
    # test()
    # exit(1)
    a, b = map(int, input().split())
    print(lcm(a, b))

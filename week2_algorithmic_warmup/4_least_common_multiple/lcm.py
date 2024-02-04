"""
2.1.8 Least Common Multiple

Compute the least common multiple of two pos- itive integers.

Input: Two positive integers a and b.
Output: The least common mul- tiple of a and b.

"""


def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a

    # Find power of two in common
    shift = 0
    while ((a | b) & 1) == 0:
        a >>= 1
        b >>= 1
        shift += 1

    # Ensure a is odd
    while (a & 1) == 0:
        a >>= 1

    while b != 0:
        while (b & 1) == 0:
            b >>= 1
        # a and b are both odd, swap to ensure a >= b
        if a < b:
            a, b = b, a
        a = a - b
    return a << shift


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

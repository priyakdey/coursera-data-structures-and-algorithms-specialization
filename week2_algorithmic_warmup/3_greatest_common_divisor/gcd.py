"""
2.1.7 Greatest Common Divisor

Compute the greatest common divisor of two positive integers.

Input: Two positive integers a and b.
Output: The greatest common di- visor of a and b.

----

Approach 1: The simplest approach is to iterate from 1 to min(a, b).

Approach 2: Euclidean gcd algorithm
Ref: https://en.wikipedia.org/wiki/Euclidean_algorithm
The idea is based on following:
1. gcd(a, b) = gcd(b, a) -> commutative
2. gcd(a, 0) = a
3. gcd(a, b) = gcd(a', b), where a' = a % b

Approach 3: Binary GCD or Stein's Algorithm
Ref: https://en.wikipedia.org/wiki/Binary_GCD_algorithm
This is an extension of Euclidean algorithm, but faster byt replacing
mod with shifting and subtraction operation

1. gcd(a, 0) = a                            , b == 0
2. gcd(2a, 2b) = 2 * gcd(a, b)              , a and b = even
3. gcd(2a, b) = gcd(a, b)                   , a = even and b = odd
4. gcd(a, 2b) = gcd(a, b)                   , a = odd and b = even
5. gcd(a, b) = gcd(abs(a - b), min(a, b))   , a and b = odd

"""


def gcd(a: int, b: int) -> int:
    # always make sure a is larger value and b is the lesser value
    if a < b:
        a, b = b, a

    if b == 0:
        return a

    gcd = 1
    while a & 1 == 0 and b & 1 == 0:
        gcd = gcd << 1
        a = a >> 1
        b = b >> 1

    while a & 1 == 0:
        a = a >> 1
    while b & 1 == 0:
        b = b >> 1

    while b != 0:
        a = a - b
        while a & 1 == 0 and a > 0:
            a = a >> 1
        if a < b:
            a, b = b, a

    return a * gcd


def gcd_euclidean(a: int, b: int) -> int:
    if b == 0:
        return a
    return gcd_euclidean(b, a % b)


def gcd_slow(a: int, b: int) -> int:
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def test():
    result = gcd_slow(28851538, 1183019)
    print(result)
    assert 17657 == result

    result = gcd_euclidean(28851538, 1183019)
    print(result)
    assert 17657 == result

    result = gcd(28851538, 1183019)
    print(result)
    assert 17657 == result


if __name__ == "__main__":
    # test()
    # exit(1)
    a, b = map(int, input().split())
    print(gcd(a, b))

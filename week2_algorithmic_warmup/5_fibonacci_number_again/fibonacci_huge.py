"""
2.1.3 Huge Fibonacci Number Huge Fibonacci Number Problem

Input: Integers n and m. 
Output: n-th Fibonacci number modulo m.

----

Pisano Period: When fibonacci sequence is mod with a number x, after some sequences,
the sequence repeats.
This distance after which cycle repeats is different for each x. This distance
is called Pisano Period. This helps work with huge value of n,
without actually computing all the n terms.

"""


def find_pisano_period(m: int) -> int:
    """Returns the Pisano Period for a Fib sequence when mod with m"""

    previous, current = 0, 1
    pisano_period = -1
    for i in range(m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            pisano_period = i + 1
            break

    return pisano_period


def fibonacci_huge_naive(n: int, m: int):
    if n <= 1:
        return n

    pisano_period = find_pisano_period(m)
    n = n % pisano_period

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, (previous + current) % m

    return current


def test():
    result = fibonacci_huge_naive(1, 239)
    print(result)
    assert 1 == result

    result = fibonacci_huge_naive(115, 1000)
    print(result)
    assert 885 == result

    result = fibonacci_huge_naive(2816213588, 239)
    print(result)
    assert 151 == result


if __name__ == "__main__":
    # test()
    # exit(1)
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))

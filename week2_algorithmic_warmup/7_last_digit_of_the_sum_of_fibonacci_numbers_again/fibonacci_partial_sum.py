"""
2.1.5 Last Digit of the Partial Sum of Fibonacci Numbers

Compute the last digit of Fm +Fm+1 +···+Fn.

Input: Integers m ≤ n.
Output: The last digit of Fm + Fm+1 +···+Fn.

---
Approach:
Summation of F(0)..F(n) = F(n + 2) - 1

So summation from F(m)..F(n) = (F(0)..F(n)) - (F(0)..F(m - 1))
F(0)..F(n) = F(n + 2) - 1
F(0)..F(m - 1) = F(m + 1) - 1

"""

# Uses python3
import sys


def find_pisano_period(m: int) -> int:
    previous, current = 0, 1
    pisano_period = -1
    for i in range(m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            pisano_period = i + 1
            break

    return pisano_period


def fibonacci_last_digit(n: int) -> int:
    pisano_period = find_pisano_period(10)
    n = n % pisano_period
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, (previous + current) % 10

    return current


def fibonacci_partial_sum_naive(from_: int, to: int) -> int:
    from_plus_1_last_digit = fibonacci_last_digit(from_ + 1)
    to_plus_2_last_digit = fibonacci_last_digit(to + 2)
    return ((to_plus_2_last_digit - 1) - (from_plus_1_last_digit - 1)) % 10


def test():
    result = fibonacci_partial_sum_naive(3, 7)
    print(result)
    assert 1 == result

    result = fibonacci_partial_sum_naive(10, 10)
    print(result)
    assert 5 == result


if __name__ == "__main__":
    # test()
    # exit(1)
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))

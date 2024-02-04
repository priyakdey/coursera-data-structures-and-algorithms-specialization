"""
2.1.6 Last Digit of the Sum of Squares of Fibonacci Num- bers

Compute the last digit of F02 +F12 +···+Fn2.

Input: An integer n.
Output: The last digit of F02 + F12 + ···+Fn2.

----

Approach:
Summation of square of 1st n terms = F(n) * F(n + 1)

"""


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


def fibonacci_sum_squares(n: int) -> int:
    if n <= 1:
        return n

    n_term_last_digit = fibonacci_last_digit(n)
    n_plus_1_term_last_digit = fibonacci_last_digit(n + 1)
    return (n_term_last_digit * n_plus_1_term_last_digit) % 10


def test():
    result = fibonacci_sum_squares(7)
    print(result)
    assert 3 == result

    result = fibonacci_sum_squares(73)
    print(result)
    assert 1 == result

    result = fibonacci_sum_squares(1234567890)
    print(result)
    assert 0 == result


if __name__ == "__main__":
    # test()
    # exit(1)
    n = int(input())
    print(fibonacci_sum_squares(n))

"""
2.1.4 Last Digit of the Sum of Fibonacci Numbers

Compute the last digit of F0 +F1 +···+Fn.

Input: An integer n.
Output: The last digit of F0 + F1 + ···+Fn.

----
Approach: Summation of F(0)..F(n) = F(n + 2) - 1

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


def fibonacci_sum(n: int) -> int:
    if n <= 1:
        return n

    fibonacci_n_plus_2_last_digit = fibonacci_last_digit(n + 2)
    return fibonacci_n_plus_2_last_digit - 1


def test():
    result = fibonacci_sum(3)
    print(result)
    assert 4 == result

    result = fibonacci_sum(100)
    print(result)
    assert 5 == result


if __name__ == "__main__":
    # test()
    # exit(1)
    n = int(input())
    print(fibonacci_sum(n))

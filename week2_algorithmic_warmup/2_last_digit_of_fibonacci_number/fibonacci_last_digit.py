"""
2.1.2 Last Digit of Fibonacci Number

Compute the last digit of the n-th Fibonacci number.

Input: An integer n.
Output: The last digit of the n-th Fibonacci number.
"""


def fibonacci_last_digit(n: int) -> int:
    if n <= 1:
        return n

    previous, current = 0, 1

    for _ in range(2, n + 1):
        previous, current = current, (previous + current) % 10

    return current


def test():
    result = fibonacci_last_digit(3)
    print(result)
    assert 2 == result

    result = fibonacci_last_digit(139)
    print(result)
    assert 1 == result

    result = fibonacci_last_digit(91239)
    print(result)
    assert 6 == result


if __name__ == "__main__":
    # test()
    # exit(1)
    n = int(input())
    print(fibonacci_last_digit(n))

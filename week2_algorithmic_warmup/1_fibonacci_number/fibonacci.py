"""
2.1.1 Fibonacci Number

Compute the n-th Fibonacci number. Input: An integer n.
Output: n-th Fibonacci number.
"""


def fibonacci_number(n: int) -> int:
    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(2, n + 1):
        previous, current = current, previous + current

    return current


def test():
    result = fibonacci_number(3)
    print(result)
    assert 2 == result

    result = fibonacci_number(10)
    print(result)
    assert 55 == result


if __name__ == "__main__":
    # test()
    # exit(1)
    input_n = int(input())
    print(fibonacci_number(input_n))

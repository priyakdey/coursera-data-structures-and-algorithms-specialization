"""
Maximum Pairwise Product Problem

Find the maximum product of two distinct numbers in a sequence of non-negative 
integers.

Input: An integer n and a sequence of n non-negative integers.

Output: The maximum value
that can be obtained by multiplying two different elements from
the sequence.

Since array only contains non negative elements, we do not consider
the lowest values, otherwise, we need to find the min and second_min too.
The max product would be = max(max * second_max, min * second_min).

Working with python, we dont even consider ranges for int, otherwise, we
should work with long.
"""

from typing import List


def max_pairwise_product(numbers: List[int]) -> int:
    max_num = max(numbers[0], numbers[1])
    second_max_num = min(numbers[0], numbers[1])

    for i in range(2, len(numbers)):
        num = numbers[i]
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num

    return max_num * second_max_num


def max_pairwise_product_slow(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


if __name__ == "__main__":
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))

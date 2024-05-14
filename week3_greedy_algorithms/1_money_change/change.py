"""
3.2.1 Money Change

Compute the minimum number of coins needed to change the given value into coins 
with de- nominations 1, 5, and 10.

Input: An integer money. 
Output: The minimum number of coins with denominations 1, 5, and 10 that 
changes money.

Since denomination is fixed, [1, 5, 10], we can follow greedy approach and
take the biggest coin to minimize total number of coins.

"""

from typing import List


def change(money: int) -> int:
    denominations: List[int] = [10, 5, 1]
    index = 0
    coin_count = 0
    while money > 0 and index < len(denominations):
        coin = denominations[index]
        if money >= coin:
            money = money - coin
            coin_count += 1
        else:
            index += 1

    return coin_count if money == 0 else -1


def test():
    result = change(2)
    print(result)
    assert 2 == result

    result = change(28)
    print(result)
    assert 6 == result


if __name__ == "__main__":
    # test()
    # exit(1)
    m = int(input())
    print(change(m))

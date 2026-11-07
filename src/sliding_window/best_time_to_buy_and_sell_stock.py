"""
Best Time to Buy and Sell Stock  —  LC 121  —  Difficulty: Easy

Given an array `prices` where `prices[i]` is the price of a stock on day `i`,
choose ONE day to buy and a LATER day to sell. Return the maximum profit.
If no profit is possible, return 0.

Assumptions (clarified up front):
  - 1 <= len(prices) <= 10^5
  - 0 <= prices[i] <= 10^4
  - Buy day must come strictly before sell day.
  - At most one transaction; not trading at all yields 0.

Examples:
    max_profit([7, 1, 5, 3, 6, 4])  ->  5      # buy at 1, sell at 6
    max_profit([7, 6, 4, 3, 1])     ->  0      # prices only fall

Target complexity:  O(n) time, O(1) space.
"""


def max_profit(prices: list[int]) -> int:

    smallest = prices[0]
    maximum = 0

    for price in prices:
        smallest = min(price, smallest)
        profit = price - smallest
        maximum = max(maximum, profit)

    return maximum

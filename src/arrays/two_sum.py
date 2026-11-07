"""
Two Sum  —  LC 1  —  Difficulty: Easy

Given an array of integers `nums` and an integer `target`, return the INDICES
of the two numbers that add up to `target`.

Assumptions (clarified up front):
  - The array is NOT sorted.
  - Exactly one valid answer exists.
  - You may not use the same element twice.
  - Values may be negative or zero.
  - Return the two indices in any order.

Example:
    two_sum([2, 7, 11, 15], 9)  ->  [0, 1]      # 2 + 7 == 9

Target complexity:  O(n) time, O(n) space.
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [i, seen[complement]]

        seen[num] = i

    raise ValueError("no pairs sum to target")

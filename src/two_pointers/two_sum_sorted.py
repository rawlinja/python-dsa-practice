"""
Two Sum II  —  LC 167  —  Difficulty: Medium

Given an array `numbers` sorted in NON-DECREASING order (equal values may sit
next to each other), return the indices of the two numbers that add up to
`target`. The indices are 1-INDEXED and returned smallest-first:
[i, j] with i < j and numbers[i - 1] + numbers[j - 1] == target.

Assumptions (clarified up front):
  - 2 <= len(numbers) <= 3 * 10**4
  - -1000 <= numbers[i] <= 1000 and -1000 <= target <= 1000.
  - Exactly one pair sums to `target`; the same element may not be used twice.

Examples:
    two_sum_sorted([2, 7, 11, 15], 9)     ->  [1, 2]
    two_sum_sorted([-8, -5, -3, -1], -4)  ->  [3, 4]

Target complexity:  O(n) time, O(1) space; no hash map, no extra copy of the input.
"""


def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total < target:
            left += 1
        if total > target:
            right -= 1

        if total == target:
            return [left + 1, right + 1]

    raise ValueError("numbers contains no pair summing to target")

"""
Contains Duplicate  —  LC 217  —  Difficulty: Easy

Given an integer array `nums`, return True if any value appears AT LEAST TWICE,
and False if every element is distinct.

Assumptions (clarified up front):
  - The array is NOT sorted.
  - Values are 32-bit signed ints: -10**9 <= nums[i] <= 10**9 (negatives, zero ok).
  - Length: 1 <= len(nums) <= 10**5  (defensively, [] -> False).
  - Not memory-constrained; O(n) auxiliary space is acceptable.

Example:
    contains_duplicate([1, 2, 3, 1])  ->  True     # 1 repeats
    contains_duplicate([1, 2, 3, 4])  ->  False    # all distinct

Target complexity:  O(n) time, O(n) space.
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

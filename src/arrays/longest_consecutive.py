"""
Longest Consecutive Sequence  —  LC 128  —  Difficulty: Medium

Given an unsorted array of integers `nums`, return the length of the longest
run of consecutive integers (values differing by exactly 1). The values need
not be adjacent in the array: position is irrelevant, only membership.

Assumptions (clarified up front):
  - 0 <= len(nums) <= 10**5; an empty input returns 0.
  - -10**9 <= nums[i] <= 10**9; negatives allowed.
  - Duplicates do not lengthen a run: [1, 2, 0, 1] has the run 0, 1, 2 -> 3.

Examples:
    longest_consecutive([100, 4, 200, 1, 3, 2])  ->  4      # 1, 2, 3, 4
    longest_consecutive([1, 2, 4, 5, 6])         ->  3      # 4, 5, 6

Target complexity:  O(n) time, O(n) space. Sorting would be O(n log n), too slow.
"""


def longest_consecutive(nums: list[int]) -> int:
    present = set(nums)
    longest = 0

    for x in present:
        if x - 1 not in present:
            run_length = 1
            probe = x + 1
            while probe in present:
                run_length += 1
                probe += 1

            longest = max(longest, run_length)

    return longest

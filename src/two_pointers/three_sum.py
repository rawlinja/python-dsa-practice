"""
3Sum  —  LC 15  —  Difficulty: Medium

Given an integer array `nums`, return all unique triplets of values drawn from
three DISTINCT INDICES that sum to zero. Repeated values may appear in a
triplet if the array supplies enough copies: [-1, -1, 2] is valid when `nums`
holds two -1s. Two triplets are the same if they contain the same multiset of
values, regardless of indices or order; the result must contain no such pair.

Assumptions (clarified up front):
  - 3 <= len(nums) <= 3000
  - -10**5 <= nums[i] <= 10**5; not sorted. `nums` may be reordered in place.
  - No solution is guaranteed; an empty list is a valid answer.
  - Triplets, and the values inside each, may be returned in any order.

Examples:
    three_sum([-1, 0, 1, 2, -1, -4])  ->  [[-1, -1, 2], [-1, 0, 1]]
    three_sum([0, 1, 1])              ->  []
    three_sum([0, 0, 0])              ->  [[0, 0, 0]]

Target complexity:  O(n**2) time, O(n) auxiliary space (the returned list excluded).
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    i = 0
    triplets = []

    while i < n - 2:
        mid = i + 1
        right = n - 1

        target = -nums[i]

        while mid < right:
            total = nums[mid] + nums[right]
            if total < target:
                mid += 1
            elif total > target:
                right -= 1
            else:
                triplets.append([nums[i], nums[mid], nums[right]])
                mid += 1
                right -= 1

                while mid < right and nums[mid] == nums[mid - 1]:
                    mid += 1
                while mid < right and nums[right] == nums[right + 1]:
                    right -= 1

        i += 1
        while i < n - 1 and nums[i] == nums[i - 1]:
            i += 1

    return triplets

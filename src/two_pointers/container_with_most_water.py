"""
Container With Most Water  —  LC 11  —  Difficulty: Medium

Given an array `height`, where `height[i]` is the height of a vertical line at
x-coordinate `i`, find two lines that together with the x-axis form the
container holding the most water. The container cannot be slanted, so the
water level is capped by the SHORTER of the two lines:

    area(i, j) = min(height[i], height[j]) * (j - i)

Return the largest area.

Assumptions (clarified up front):
  - 2 <= len(height) <= 10**5
  - 0 <= height[i] <= 10**4; lines of height 0 hold nothing, so all zeros -> 0.

Examples:
    max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])  ->  49
    max_area([1, 1])                       ->  1

Target complexity:  O(n) time, O(1) space; a single pass, no sorting.
"""


def max_area(height: list[int]) -> int:
    left = 0
    right = len(height) - 1

    largest = 0

    while left < right:
        w = right - left
        h = min(height[left], height[right])
        area = w * h
        largest = max(largest, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return largest

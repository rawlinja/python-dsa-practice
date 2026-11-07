def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    """Find the two numbers in sorted ``numbers`` that add up to ``target`` (LC 167, Medium).

    ``numbers`` is sorted in **non-decreasing** order, so equal values may sit
    next to each other. Exactly one pair sums to ``target``, and the same
    element may not be used twice.

    The returned indices are **1-indexed**, not 0-indexed: the first element of
    ``numbers`` is at index 1. They are returned smallest-first.

    Args:
        numbers: 2 <= len(numbers) <= 3 * 10**4, sorted non-decreasing,
            each -1000 <= numbers[i] <= 1000.
        target: -1000 <= target <= 1000. A solution is guaranteed to exist.

    Returns:
        ``[i, j]`` with i < j, 1-indexed, where
        ``numbers[i - 1] + numbers[j - 1] == target``.

    Examples:
        >>> two_sum_sorted([2, 7, 11, 15], 9)
        [1, 2]
        >>> two_sum_sorted([-8, -5, -3, -1], -4)
        [3, 4]

    Target: O(n) time, O(1) space — no hash map, no extra copy of the input.
    """

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

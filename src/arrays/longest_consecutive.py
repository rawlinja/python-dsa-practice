def longest_consecutive(nums: list[int]) -> int:
    """Length of the longest run of consecutive integers in ``nums`` (LC 128, Medium).

    Consecutive means values differing by exactly 1. The values need not be
    adjacent in the array — position is irrelevant, only membership.

    Args:
        nums: 0 <= len(nums) <= 10**5, values in [-10**9, 10**9]. May contain
            duplicates and negatives; is not sorted.

    Returns:
        The length of the longest run, or 0 for an empty input. Duplicates do
        not lengthen a run: [1, 2, 0, 1] has the run 0, 1, 2 and returns 3.

    Examples:
        >>> longest_consecutive([100, 4, 200, 1, 3, 2])
        4
        >>> longest_consecutive([1, 2, 4, 5, 6])
        3

    Target: O(n) time, O(n) space. Sorting would be O(n log n) — too slow.
    """

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

def max_area(height: list[int]) -> int:
    """Most water two of the vertical lines in ``height`` can hold (LC 11, Medium).

    ``height[i]`` is the height of a vertical line standing at x-coordinate
    ``i``. Any two lines, together with the x-axis, form a container. The
    container cannot be slanted, so the water level is flat and capped by the
    **shorter** of the two lines:

        area(i, j) = min(height[i], height[j]) * (j - i)

    Args:
        height: 2 <= len(height) <= 10**5, each 0 <= height[i] <= 10**4.

    Returns:
        The largest area achievable by any pair of lines. Lines of height 0
        hold nothing, so an all-zero input returns 0.

    Examples:
        >>> max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])
        49
        >>> max_area([1, 1])
        1

    Target: O(n) time, O(1) space — a single pass, no sorting.
    """

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

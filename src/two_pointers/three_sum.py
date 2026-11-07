def three_sum(nums: list[int]) -> list[list[int]]:
    """All unique triplets in ``nums`` that sum to zero (LC 15, Medium).

    A triplet is three values drawn from three **distinct indices** whose sum is
    zero. Repeated values may appear in a triplet as long as the array supplies
    enough copies: ``[-1, -1, 2]`` is valid when ``nums`` holds two ``-1``s.

    Two triplets are the same if they contain the same multiset of values,
    regardless of the indices they came from or the order they appear in. The
    returned list must contain no such pair.

    Args:
        nums: 3 <= len(nums) <= 3000, each -10**5 <= nums[i] <= 10**5.
            Not sorted. May be reordered in place.

    Returns:
        Every distinct zero-sum triplet, in any order, each triplet's values in
        any order. No solution is guaranteed — an empty list is a valid answer.

    Examples:
        >>> sorted(three_sum([-1, 0, 1, 2, -1, -4]))
        [[-1, -1, 2], [-1, 0, 1]]
        >>> three_sum([0, 1, 1])
        []
        >>> three_sum([0, 0, 0])
        [[0, 0, 0]]

    Target: O(n**2) time, O(n) auxiliary space (the returned list excluded).
    """

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

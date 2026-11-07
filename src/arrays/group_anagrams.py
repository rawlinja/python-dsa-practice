def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Group the anagrams in ``strs`` together (LeetCode 49, Medium).

    Two strings are anagrams when they contain the same letters with the same
    multiplicities.

    Args:
        strs: 1 <= len(strs) <= 10**4, each string 0 to 100 lowercase letters.

    Returns:
        The groups, in any order, with the strings inside each group in any
        order. Every input string appears exactly once across all groups.

    Examples:
        >>> group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    Target: O(n * k) time, O(n * k) space, for n strings of average length k.
    """

    groups: dict[tuple[int, ...], list[str]] = {}
    for s in strs:
        key = tuple(letter_counts(s))
        if key not in groups:
            groups[key] = [s]
        else:
            groups[key].append(s)

    return list(groups.values())


def letter_counts(s: str) -> list[int]:
    counts = [0] * 26
    for c in s:
        counts[ord(c) - ord("a")] += 1
    return counts

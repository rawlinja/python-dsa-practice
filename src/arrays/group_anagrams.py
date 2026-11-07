"""
Group Anagrams  —  LC 49  —  Difficulty: Medium

Given an array of strings `strs`, group the anagrams together. Two strings are
anagrams when they contain the same letters with the same multiplicities.
Return the groups in any order, with the strings inside each group in any
order. Every input string appears exactly once across all groups.

Assumptions (clarified up front):
  - 1 <= len(strs) <= 10**4
  - Each string is 0 to 100 lowercase English letters.

Example:
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        ->  [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Target complexity:  O(n * k) time, O(n * k) space, for n strings of average length k.
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
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

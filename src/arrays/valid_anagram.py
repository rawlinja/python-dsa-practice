"""
Valid Anagram  —  LC 242  —  Difficulty: Easy

Given two strings `s` and `t`, return True if `t` is an anagram of `s`, and
False otherwise. An anagram uses exactly the same characters with the same
counts, in any order.

Assumptions (clarified up front):
  - Characters are lowercase English letters only ('a'..'z').
  - No uppercase, spaces, punctuation, or Unicode.
  - Lengths: 0 <= len(s), len(t) <= 5 * 10**4; lengths may differ.
  - Two empty strings are anagrams of each other.

Example:
    is_anagram("anagram", "nagaram")  ->  True
    is_anagram("rat", "car")          ->  False

Target complexity:  O(n) time, O(1) space.
"""


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    frequency: dict[str, int] = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in t:
        if ch not in frequency:
            return False

        if frequency.get(ch) == 0:
            return False

        frequency[ch] = frequency.get(ch, 0) - 1

    return True

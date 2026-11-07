import pytest

from arrays.group_anagrams import group_anagrams


def normalized(groups: list[list[str]]) -> list[list[str]]:
    """Order-insensitive form, since the problem allows any ordering.

    Apply to both sides of an assertion so expectations can be written in
    whatever order reads best.
    """
    return sorted(sorted(group) for group in groups)


def test_groups_anagrams_together() -> None:
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

    assert normalized(result) == normalized([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])


def test_single_empty_string() -> None:
    assert group_anagrams([""]) == [[""]]


def test_single_character() -> None:
    assert group_anagrams(["a"]) == [["a"]]


def test_all_strings_are_anagrams() -> None:
    result = group_anagrams(["abc", "bca", "cab"])

    assert normalized(result) == normalized([["abc", "bca", "cab"]])


def test_no_strings_are_anagrams() -> None:
    result = group_anagrams(["abc", "de", "f"])

    assert normalized(result) == normalized([["abc"], ["de"], ["f"]])


def test_duplicate_strings_stay_in_the_same_group() -> None:
    result = group_anagrams(["ab", "ba", "ab"])

    assert normalized(result) == normalized([["ab", "ba", "ab"]])


def test_letter_counts_above_nine_do_not_collide() -> None:
    """Counts (1, 11) and (11, 1) are different signatures, not one group."""
    result = group_anagrams(["a" + "b" * 11, "a" * 11 + "b"])

    assert normalized(result) == normalized([["abbbbbbbbbbb"], ["aaaaaaaaaaab"]])


@pytest.mark.parametrize(
    "strs",
    [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        ["abc", "de", "f", ""],
        ["ab", "ba", "ab"],
    ],
)
def test_every_input_appears_exactly_once(strs: list[str]) -> None:
    result = group_anagrams(strs)

    assert sorted(s for group in result for s in group) == sorted(strs)

import pytest

from two_pointers.two_sum_sorted import two_sum_sorted


def test_leetcode_example() -> None:
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]


def test_indices_are_one_indexed_not_zero_indexed() -> None:
    """A 0-indexed implementation returns [0, 1] here and fails."""
    assert two_sum_sorted([1, 2], 3) == [1, 2]


def test_smallest_possible_input() -> None:
    assert two_sum_sorted([-1, 0], -1) == [1, 2]


def test_pair_sits_at_both_ends() -> None:
    assert two_sum_sorted([1, 2, 3, 4, 9], 10) == [1, 5]


def test_pair_sits_adjacent_in_the_middle() -> None:
    assert two_sum_sorted([1, 5, 6, 20], 11) == [2, 3]


def test_pair_skips_over_the_first_element() -> None:
    assert two_sum_sorted([2, 3, 4], 6) == [1, 3]


def test_duplicate_values_form_the_pair() -> None:
    assert two_sum_sorted([3, 3], 6) == [1, 2]


def test_duplicate_values_at_the_front() -> None:
    assert two_sum_sorted([0, 0, 3, 4], 0) == [1, 2]


def test_negatives_and_positives_mixed() -> None:
    assert two_sum_sorted([-5, -3, 0, 2, 8], 5) == [2, 5]


def test_all_negative_values() -> None:
    assert two_sum_sorted([-8, -5, -3, -1], -4) == [3, 4]


def test_pair_straddles_zero() -> None:
    assert two_sum_sorted([-7, -2, 1, 4, 9], -1) == [2, 3]


@pytest.mark.parametrize(
    ("numbers", "target", "expected"),
    [
        ([1, 4], 5, [1, 2]),
        ([1, 2, 3], 5, [2, 3]),
        ([-1000, 0, 1000], 0, [1, 3]),
        ([1, 3, 5, 7, 9], 8, [1, 4]),
    ],
)
def test_small_cases(numbers: list[int], target: int, expected: list[int]) -> None:
    assert two_sum_sorted(numbers, target) == expected


def test_long_input_with_the_pair_at_the_far_left() -> None:
    numbers = list(range(1, 30_001))
    assert two_sum_sorted(numbers, 3) == [1, 2]


def test_long_input_with_the_pair_at_the_far_right() -> None:
    numbers = list(range(1, 30_001))
    assert two_sum_sorted(numbers, 59_999) == [29_999, 30_000]

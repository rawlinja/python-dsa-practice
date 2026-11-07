from collections import Counter

import pytest

from two_pointers.three_sum import three_sum


def canonical(triplets: list[list[int]]) -> list[tuple[int, ...]]:
    """Order-insensitive form: triplets sorted internally, then as a whole."""
    return sorted(tuple(sorted(triplet)) for triplet in triplets)


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([1, 2, 3], []),
        ([-1, 0, 1], [[-1, 0, 1]]),
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    ],
)
def test_small_cases(nums: list[int], expected: list[list[int]]) -> None:
    assert canonical(three_sum(nums)) == canonical(expected)


def test_no_triplet_exists() -> None:
    assert three_sum([1, 2, -2, -1]) == []


def test_all_positive_can_never_sum_to_zero() -> None:
    assert three_sum([5, 5, 5, 5, 5]) == []


def test_triplet_may_reuse_a_repeated_value() -> None:
    assert canonical(three_sum([-1, -1, 2])) == [(-1, -1, 2)]


def test_repeated_values_on_both_sides_yield_one_triplet() -> None:
    assert canonical(three_sum([-2, 0, 0, 2, 2])) == [(-2, 0, 2)]


def test_every_element_identical() -> None:
    assert canonical(three_sum([0, 0, 0, 0, 0, 0])) == [(0, 0, 0)]


def test_many_duplicates_collapse() -> None:
    """Three zeroes are three distinct slots, so [0, 0, 0] is its own triplet."""
    nums = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    assert canonical(three_sum(nums)) == [(-1, 0, 1), (0, 0, 0)]


def test_result_contains_no_duplicate_triplets() -> None:
    nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    result = canonical(three_sum(nums))

    assert len(result) == len(set(result))


def test_every_returned_triplet_sums_to_zero() -> None:
    nums = [-5, -3, -1, 0, 1, 2, 3, 4, 5, -2, 2]

    for triplet in three_sum(nums):
        assert len(triplet) == 3
        assert sum(triplet) == 0


def test_returned_values_are_available_in_the_input() -> None:
    """A triplet may not use one array slot twice."""
    nums = [-1, -1, 2, 0, 1]
    available = Counter(nums)

    for triplet in three_sum(nums):
        used = Counter(triplet)
        assert all(used[value] <= available[value] for value in used)


def test_long_input_requires_a_quadratic_solution() -> None:
    nums = list(range(1, 1501))

    assert three_sum(nums) == []

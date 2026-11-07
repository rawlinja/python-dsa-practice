import pytest

from arrays.longest_consecutive import longest_consecutive


def test_run_scattered_across_the_array() -> None:
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4


def test_longer_example() -> None:
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_empty_input() -> None:
    assert longest_consecutive([]) == 0


def test_single_element_is_a_run_of_one() -> None:
    assert longest_consecutive([7]) == 1


def test_duplicates_do_not_lengthen_a_run() -> None:
    assert longest_consecutive([1, 2, 0, 1]) == 3


def test_all_duplicates() -> None:
    assert longest_consecutive([5, 5, 5]) == 1


def test_longest_of_several_runs_wins() -> None:
    assert longest_consecutive([1, 2, 4, 5, 6]) == 3


def test_earlier_run_is_not_overwritten_by_a_shorter_later_one() -> None:
    assert longest_consecutive([1, 2, 3, 4, 10, 20]) == 4


def test_negatives_and_zero() -> None:
    assert longest_consecutive([-2, -1, 0, 5]) == 3


def test_run_spanning_zero() -> None:
    assert longest_consecutive([1, -1, 0, -2, 9]) == 4


def test_two_groups_bridged_by_a_later_value() -> None:
    """[1,2] and [5,6] are separate until 3 and 4 fuse them into one run."""
    assert longest_consecutive([1, 2, 5, 6, 3, 4]) == 6


def test_no_consecutive_values_at_all() -> None:
    assert longest_consecutive([10, 30, 20, 50]) == 1


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1], 1),
        ([2, 1], 2),
        ([1, 3], 1),
        ([1000000000, 999999999], 2),
        ([-1000000000, -999999999], 2),
    ],
)
def test_small_and_boundary_cases(nums: list[int], expected: int) -> None:
    assert longest_consecutive(nums) == expected

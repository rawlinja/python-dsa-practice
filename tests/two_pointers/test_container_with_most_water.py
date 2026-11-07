import pytest

from two_pointers.container_with_most_water import max_area


def test_leetcode_example() -> None:
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_smallest_possible_input() -> None:
    assert max_area([1, 1]) == 1


def test_two_lines_of_different_height() -> None:
    assert max_area([1, 2]) == 1


def test_widest_pair_wins() -> None:
    assert max_area([4, 3, 2, 1, 4]) == 16


def test_narrow_and_deep_beats_wide_and_shallow() -> None:
    assert max_area([1, 100, 100, 1]) == 100


def test_wide_and_shallow_beats_narrow_and_deep() -> None:
    assert max_area([100, 1, 1, 1, 100]) == 400


def test_best_pair_is_interior() -> None:
    assert max_area([1, 3, 2, 5, 25, 24, 5]) == 24


def test_zero_height_holds_nothing() -> None:
    assert max_area([0, 2]) == 0


def test_all_zero_heights() -> None:
    assert max_area([0, 0, 0, 0]) == 0


def test_strictly_increasing() -> None:
    assert max_area([1, 2, 3, 4, 5]) == 6


def test_strictly_decreasing() -> None:
    assert max_area([5, 4, 3, 2, 1]) == 6


def test_single_peak_between_flats() -> None:
    assert max_area([1, 2, 1]) == 2


@pytest.mark.parametrize(
    ("height", "expected"),
    [
        ([2, 3, 4, 5, 18, 17, 6], 17),
        ([1, 2, 4, 3], 4),
        ([2, 1], 1),
        ([0, 1, 0], 0),
    ],
)
def test_small_cases(height: list[int], expected: int) -> None:
    assert max_area(height) == expected


def test_long_input_requires_a_linear_solution() -> None:
    """A quadratic solution will not finish this — 10**5 lines is 5 * 10**9 pairs."""
    height = list(range(1, 100_001))
    assert max_area(height) == 2_500_000_000

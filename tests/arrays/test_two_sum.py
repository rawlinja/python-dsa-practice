import pytest

from arrays.two_sum import two_sum


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([0, 4, 3, 0], 0, [0, 3]),
    ],
)
def test_two_sum(nums: list[int], target: int, expected: list[int]) -> None:
    # indices may be returned in any order
    assert sorted(two_sum(nums, target)) == sorted(expected)

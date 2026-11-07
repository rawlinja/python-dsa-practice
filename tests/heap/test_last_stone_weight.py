from heap.last_stone_weight import last_stone_weight


def test_example():
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1


def test_single_stone_returns_its_weight():
    assert last_stone_weight([1000]) == 1000


def test_two_equal_stones_destroy_each_other():
    assert last_stone_weight([3, 3]) == 0


def test_two_unequal_stones_leave_the_difference():
    assert last_stone_weight([10, 4]) == 6


def test_even_count_of_equal_stones_leaves_nothing():
    assert last_stone_weight([4, 4, 4, 4]) == 0


def test_odd_count_of_equal_stones_leaves_one():
    assert last_stone_weight([4, 4, 4]) == 4


def test_smashes_heaviest_not_lightest():
    assert last_stone_weight([1, 1, 10]) == 8


def test_equal_pair_first_then_leftovers():
    assert last_stone_weight([8, 8, 3, 1]) == 2


def test_equal_pair_leaves_single_stone():
    assert last_stone_weight([2, 2, 1]) == 1


def test_remainder_rejoins_and_is_smashed_again():
    assert last_stone_weight([7, 6, 7, 6, 9]) == 3


def test_chain_ends_in_mutual_destruction():
    assert last_stone_weight([9, 3, 2, 10]) == 0


def test_ascending_input():
    assert last_stone_weight([1, 2, 3, 4, 5]) == 1


def test_extreme_weights():
    assert last_stone_weight([1000, 1]) == 999


def test_max_length_even_all_equal():
    assert last_stone_weight([1000] * 30) == 0


def test_max_length_odd_all_equal():
    assert last_stone_weight([1000] * 29) == 1000

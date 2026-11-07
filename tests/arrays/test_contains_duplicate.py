from arrays.contains_duplicate import contains_duplicate


def test_returns_true_when_a_value_repeats():
    assert contains_duplicate([1, 2, 3, 1]) is True


def test_returns_false_when_all_distinct():
    assert contains_duplicate([1, 2, 3, 4]) is False


def test_single_element_has_no_duplicate():
    assert contains_duplicate([7]) is False


def test_empty_array_has_no_duplicate():
    assert contains_duplicate([]) is False


def test_duplicate_can_be_far_apart():
    assert contains_duplicate([1, 5, 9, 3, 2, 8, 1]) is True


def test_handles_negatives_and_zero():
    assert contains_duplicate([-3, 0, 3, -3]) is True
    assert contains_duplicate([-3, 0, 3, 7]) is False


def test_all_same_value():
    assert contains_duplicate([4, 4, 4, 4]) is True

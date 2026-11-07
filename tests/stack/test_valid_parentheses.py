from stack.valid_parentheses import is_valid


def test_single_pair():
    assert is_valid("()")


def test_each_bracket_type_in_sequence():
    assert is_valid("()[]{}")


def test_mismatched_type():
    assert not is_valid("(]")


def test_interleaved_pairs_are_invalid():
    assert not is_valid("([)]")


def test_fully_nested():
    assert is_valid("{[()]}")


def test_nested_and_sequential_mixed():
    assert is_valid("([]){[()()]}")


def test_single_opener():
    assert not is_valid("(")


def test_single_closer():
    assert not is_valid("]")


def test_closer_first_then_balanced():
    assert not is_valid(")(")


def test_leftover_opener_at_end():
    assert not is_valid("()[")


def test_extra_closer_after_balanced():
    assert not is_valid("()]")


def test_all_openers():
    assert not is_valid("(((((")


def test_all_closers():
    assert not is_valid(")))))")


def test_deep_nesting():
    assert is_valid("(" * 5000 + ")" * 5000)


def test_odd_length_cannot_be_valid():
    assert not is_valid("(()")

from arrays.valid_anagram import is_anagram


def test_true_for_a_valid_anagram():
    assert is_anagram("anagram", "nagaram") is True


def test_false_when_characters_differ():
    assert is_anagram("rat", "car") is False


def test_false_when_lengths_differ():
    assert is_anagram("aab", "ab") is False


def test_false_when_same_letters_wrong_counts():
    assert is_anagram("aabb", "abbb") is False


def test_true_for_two_empty_strings():
    assert is_anagram("", "") is True


def test_false_when_t_has_an_extra_char():
    assert is_anagram("ab", "abc") is False


def test_true_when_identical_strings():
    assert is_anagram("listen", "listen") is True

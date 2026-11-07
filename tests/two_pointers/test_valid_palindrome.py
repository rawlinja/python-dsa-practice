import pytest

from two_pointers.valid_palindrome import is_palindrome


def test_classic_phrase_with_punctuation_and_case() -> None:
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_phrase_that_is_not_a_palindrome() -> None:
    assert is_palindrome("race a car") is False


def test_only_whitespace_is_vacuously_a_palindrome() -> None:
    assert is_palindrome(" ") is True


def test_only_punctuation_is_vacuously_a_palindrome() -> None:
    assert is_palindrome(".,;:!?") is True


def test_single_character() -> None:
    assert is_palindrome("a") is True


def test_digits_count_as_alphanumeric() -> None:
    assert is_palindrome("0P") is False


def test_numeric_palindrome() -> None:
    assert is_palindrome("12321") is True


def test_mixed_letters_and_digits() -> None:
    assert is_palindrome("a1b2b1a") is True


def test_run_of_punctuation_between_matching_characters() -> None:
    """A single skip is not enough — the run must be walked to its end."""
    assert is_palindrome("a,,,,a") is True


def test_leading_punctuation_before_the_first_letter() -> None:
    assert is_palindrome(",a") is True


def test_trailing_punctuation_after_the_last_letter() -> None:
    assert is_palindrome("a.") is True


def test_case_is_folded_on_both_sides() -> None:
    assert is_palindrome("AbBa") is True


def test_even_length_palindrome() -> None:
    assert is_palindrome("abba") is True


def test_odd_length_palindrome() -> None:
    assert is_palindrome("aba") is True


def test_mismatch_at_the_very_centre() -> None:
    assert is_palindrome("abcba!x") is False


def test_mismatch_only_at_the_outermost_pair() -> None:
    assert is_palindrome("xbbay") is False


@pytest.mark.parametrize(
    ("s", "expected"),
    [
        ("ab", False),
        ("aa", True),
        ("a b a", True),
        ("Zz", True),
        ("1a2", False),
    ],
)
def test_small_cases(s: str, expected: bool) -> None:
    assert is_palindrome(s) is expected


def test_long_input_does_not_blow_up() -> None:
    half = "ab1c" * 25_000
    assert is_palindrome(half + half[::-1]) is True

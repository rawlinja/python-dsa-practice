def is_palindrome(s: str) -> bool:
    """Whether ``s`` reads the same forwards and backwards (LC 125, Easy).

    Only alphanumeric characters count — letters ``a-z``/``A-Z`` and digits
    ``0-9``. Everything else (spaces, punctuation) is ignored, and case is
    folded, so ``'A'`` and ``'a'`` are the same character.

    Args:
        s: 1 <= len(s) <= 2 * 10**5, printable ASCII only.

    Returns:
        True if the alphanumeric characters of ``s``, lowercased, read the
        same in both directions. A string with no alphanumeric characters
        (" ") is vacuously a palindrome and returns True.

    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False

    Target: O(n) time, O(1) space — no cleaned copy of the input.
    """

    start = 0
    end = len(s) - 1

    while start < end:
        while not s[start].isalnum() and start < end:
            start += 1
        while not s[end].isalnum() and start < end:
            end -= 1

        if s[start].lower() != s[end].lower():
            return False

        start = start + 1
        end = end - 1

    return True

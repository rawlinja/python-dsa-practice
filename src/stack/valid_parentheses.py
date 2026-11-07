"""
Valid Parentheses  —  LC 20  —  Difficulty: Easy

Given a string `s` containing only the characters '(', ')', '{', '}', '[' and ']',
return True if the string is valid. A string is valid when:
  1. Every opening bracket is closed by a bracket of the same type.
  2. Brackets are closed in the correct order.
  3. Every closing bracket has a corresponding opening bracket.

Assumptions (clarified up front):
  - 1 <= len(s) <= 10^4
  - `s` contains only the six bracket characters.

Examples:
    is_valid("()")        ->  True
    is_valid("()[]{}")    ->  True
    is_valid("(]")        ->  False
    is_valid("([)]")      ->  False    # right counts, wrong order
    is_valid("{[()]}")    ->  True

Target complexity:  O(n) time, O(n) space.
"""


def is_valid(s: str) -> bool:
    opener_for = {"}": "{", "]": "[", ")": "("}

    unclosed: list[str] = []

    for char in s:
        if char not in opener_for:
            unclosed.append(char)
        elif not unclosed or unclosed.pop() != opener_for[char]:
            return False

    return not unclosed

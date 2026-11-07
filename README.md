# Python DSA Practice

Data structures and algorithms problems in Python, solved test-first in the style of a coding interview.

## How this repo works

Each problem is a practice round in the style of a coding interview: clarify the problem, work out an approach and its complexity, then implement it against the tests.

- **Problem scaffolding** (a typed stub with the problem statement, assumptions and target complexity, plus a failing pytest suite) was generated with Claude acting as the interviewer.
- **Every solution is my own implementation**, written without AI-generated code. Claude reviewed it only after the tests passed.
- Only the latest attempt at a problem is published.

## Problems

| # | Problem | Pattern | Complexity (time / space) |
|---|---|---|---|
| 1 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) (LC 217) | [Arrays & hashing](src/arrays) | O(n) / O(n) |
| 2 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) (LC 242) | [Arrays & hashing](src/arrays) | O(n) / O(1) |
| 3 | [Two Sum](https://leetcode.com/problems/two-sum/) (LC 1) | [Arrays & hashing](src/arrays) | O(n) / O(n) |
| 4 | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) (LC 49) | [Arrays & hashing](src/arrays) | O(n·k) / O(n·k) |
| 5 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) (LC 128) | [Arrays & hashing](src/arrays) | O(n) / O(n) |
| 6 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) (LC 125) | [Two pointers](src/two_pointers) | O(n) / O(1) |
| 7 | [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) (LC 167) | [Two pointers](src/two_pointers) | O(n) / O(1) |
| 8 | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) (LC 11) | [Two pointers](src/two_pointers) | O(n) / O(1) |
| 9 | [3Sum](https://leetcode.com/problems/3sum/) (LC 15) | [Two pointers](src/two_pointers) | O(n²) / O(n) |
| 10 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) (LC 121) | [Sliding window](src/sliding_window) | O(n) / O(1) |
| 11 | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) (LC 20) | [Stack](src/stack) | O(n) / O(n) |
| 12 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) (LC 1046) | [Heap](src/heap) | O(n log n) / O(n) |

Each problem is `src/<pattern>/<problem>.py` (the solution, with the problem statement in its docstring) and `tests/<pattern>/test_<problem>.py`.

## Stack

Python 3.14 · uv · pytest · ruff · pyright (standard mode). No runtime dependencies.

## Running

```bash
uv sync --extra dev
uv run ruff check . && uv run pyright && uv run pytest   # lint, type-check, test
uv run pytest tests/two_pointers/test_three_sum.py       # one problem
```

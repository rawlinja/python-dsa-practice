"""
Last Stone Weight  —  LC 1046  —  Difficulty: Easy

Given an array `stones` where `stones[i]` is the weight of the i-th stone,
repeatedly smash the two heaviest stones together. With weights x <= y:
  - if x == y, both stones are destroyed;
  - if x != y, the x stone is destroyed and the y stone's weight becomes y - x.
Return the weight of the last remaining stone, or 0 if none remain.

Assumptions (clarified up front):
  - 1 <= len(stones) <= 30
  - 1 <= stones[i] <= 1000, integers
  - The two heaviest are re-chosen every turn.

Examples:
    last_stone_weight([2, 7, 4, 1, 8, 1])  ->  1
    last_stone_weight([1])                 ->  1
    last_stone_weight([3, 3])              ->  0

Target complexity:  O(n log n) time, O(n) space.
"""

import heapq


def last_stone_weight(stones: list[int]) -> int:
    heap = stones[:]
    heapq.heapify_max(heap)

    while len(heap) > 1:
        y = heapq.heappop_max(heap)
        x = heapq.heappop_max(heap)

        if x != y:
            heapq.heappush_max(heap, y - x)

    return heap[0] if heap else 0

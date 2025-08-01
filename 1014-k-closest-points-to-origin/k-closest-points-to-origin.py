import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            dist = -(x * x + y * y)  # Negative distance to simulate max-heap
            heapq.heappush(max_heap, (dist, x, y))  # Push into heap

            if len(max_heap) > k:
                heapq.heappop(max_heap)  # Remove the farthest point

        # Extract only the coordinates from the heap
        return [[x, y] for (_, x, y) in max_heap]

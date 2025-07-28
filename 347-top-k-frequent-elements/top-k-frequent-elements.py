class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for num, freq in count.items():
            heapq.heappush(heap, (freq,num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [num for freq, num in heap]

        # count = Counter(nums)
        # heap = []

        # for num, freq in count.items():
        #     heapq.heappush(heap, (freq, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # return [num for freq, num in heap]






















# count = {1: 3, 2: 2, 3: 1}




# Action                  | Heap Content
# ------------------------|---------------------------
# Push (3, 1)             | [(3, 1)]
# Push (2, 2)             | [(2, 2), (3, 1)]
# Push (1, 3)             | [(1, 3), (3, 1), (2, 2)]
# Pop smallest (1, 3)     | [(2, 2), (3, 1)]

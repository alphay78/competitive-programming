from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {num: i for i, num in enumerate(arr)}
        dp = {}
        max_length = 0

        for k, val_k in enumerate(arr):
            for j in range(k):
                val_j = arr[j]
                val_i = val_k - val_j
                
                if val_i in index and index[val_i] < j:
                    i = index[val_i]
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    max_length = max(max_length, dp[(j, k)])

        return max_length if max_length >= 3 else 0


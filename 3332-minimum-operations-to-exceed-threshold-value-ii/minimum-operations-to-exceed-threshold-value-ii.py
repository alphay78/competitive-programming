class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = nums.copy()
        heapify(heap)
        res = 0
        while heap[0] < k:
            x = heappop(heap)
            y = heappop(heap)
            heappush(heap , 2*x + y)
            res+=1
        return res



       

            
    
        
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        left = 0
        current_sum = 0


        for i,num in enumerate(nums):
            current_sum += num
            while current_sum >= target:
                min_length = min(min_length ,i-left+1)
                current_sum -= nums[left]
                left += 1
        return min_length if min_length != float('inf') else 0

        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        long= 0

        for num in nums:
            if num - 1 not in nums:
                current = 1
                while num + current in nums:
                    current += 1
                long = max(long, current)

        return long

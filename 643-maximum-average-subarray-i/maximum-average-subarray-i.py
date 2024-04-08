class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        res=float("-inf")
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            while i - l + 1 > k:
                temp -= nums[l]
                l += 1
            if i - l + 1 == k:
                res = max(res,temp /k)
        return res



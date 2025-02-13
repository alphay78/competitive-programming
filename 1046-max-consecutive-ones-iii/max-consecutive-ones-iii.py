class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        total = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                k-=1
            total+=1

            while k < 0:
                if nums[l]==0:
                    k+=1
                total-=1
                l+=1
            count = max(count,total)
        return count


        
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        l = 0
        r = 1

        while r < len(nums):
            if nums[l] != nums[r]:
                l+=1
                r+=1
            elif nums[l] == nums[r]:
                nums[l] = nums[l]*2
                nums[r]=0
                l+=1
                r+=1
        new_nums =[]
        for i in nums:
            if i != 0:
                new_nums.append(i)
        diff = len(nums) -len(new_nums)
        new_nums .extend([0]*diff)

        return new_nums


        
        return nums
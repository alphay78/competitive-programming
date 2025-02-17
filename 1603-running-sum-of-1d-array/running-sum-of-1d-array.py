class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre_sum=0
        new_nums =[0 for i in range(len(nums))]

        for i in range(len(nums)):
            new_nums[i] = nums[i]+pre_sum
            pre_sum = new_nums[i]
        return new_nums
            


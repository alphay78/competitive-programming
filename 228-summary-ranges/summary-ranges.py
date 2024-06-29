class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        
        new_list = []
        start = nums[0]
        
        for i in range(1, len(nums) + 1):
            if i < len(nums) and nums[i] == nums[i - 1] + 1:
                continue
            else:
                if start == nums[i - 1]:
                    new_list.append(str(start))
                else:
                    new_list.append("{}->{}".format(start, nums[i - 1]))
                if i < len(nums):
                    start = nums[i]
        
        return new_list



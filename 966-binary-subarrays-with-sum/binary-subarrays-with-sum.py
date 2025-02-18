class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        pre_sum = 0
        my_dict = {0:1}
        for i in nums:
            pre_sum+=i
            if pre_sum -  goal in my_dict:
                res += my_dict[pre_sum - goal]
            my_dict[pre_sum] = my_dict.get(pre_sum, 0) + 1
        return res


    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

# from typing import List

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         my_nums = dict(enumerate(nums))
#         count_dict = {}
#         n = len(nums)
#         result = -1  # Initialize result with a default value
        
#         for value in my_nums.values():
#             count_dict[value] = count_dict.get(value, 0) + 1

#         for value, count in count_dict.items():  # Corrected 'in.items()' to 'count_dict.items()'
#             if count > n / 2:
#                 result = value
#         return result

        
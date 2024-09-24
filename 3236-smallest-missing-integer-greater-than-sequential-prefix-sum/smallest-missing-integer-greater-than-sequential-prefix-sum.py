from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Step 1: Find the longest sequential prefix
        longest_prefix_sum = nums[0]  # Start with the first number
        
        for i in range(1, len(nums)):  # Go through the rest of the numbers
            if nums[i] == nums[i-1] + 1:  # Check if it's sequential (1 bigger than the previous one)
                longest_prefix_sum += nums[i]  # Add to the total sum
            else:
                break  # Stop if the sequence breaks

        # Step 2: Store the array elements in a set for fast lookup
        num_set = set(nums)

        # Step 3: Find the smallest missing integer >= longest_prefix_sum
        missing_number = longest_prefix_sum

        while missing_number in num_set:  # While the number is in the set
            missing_number += 1  # Move to the next number

        return missing_number

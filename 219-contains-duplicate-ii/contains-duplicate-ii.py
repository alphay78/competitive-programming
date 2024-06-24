class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        index_map = {}  # Dictionary to store the last seen index of each element

        for i, num in enumerate(nums):
            # Check if num is in the dictionary and if the difference in indices is <= k
            if num in index_map and i - index_map[num] <= k:
                return True  # Duplicate found within the range k
            
            # Update the last seen index of the current number
            index_map[num] = i

        return False  # No duplicates found within the range k
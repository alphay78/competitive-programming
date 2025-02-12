class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0  # Pointer for non-zero elements
        
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]  # Swap
                l += 1  # Move the non-zero pointer forward
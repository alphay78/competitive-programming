class Solution:
      def moveZeroes(self, nums: List[int]) -> None:
        r=1
        for i in range (len(nums)):
            if nums[i] == 0:
                r = i + 1
                while r < len(nums) and nums[r] ==0:
                    r += 1
                if r < len(nums):
                    nums[r],nums[i]=nums[i],nums[r]


    
   






   





        
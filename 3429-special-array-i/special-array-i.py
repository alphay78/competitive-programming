class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        is_special= True
        def parity(n):
            if n % 2 != 0:
                return 1
            elif n % 2 ==0:
                return 2
        if len(nums) == 1:
            return True
        else:
           
            for i in range (len (nums)-1):
                if parity(nums[i]) == parity(nums[i+1]):
                    is_special = False
                    break
        return is_special

                
        
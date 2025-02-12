class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        l =0
        r = len(nums)-1

        while l <= r:
            nums[l],nums[r] =nums[r],nums[l]
            l+=1
            r-=1
        l1 = 0
        r1 = k -1
        while l1 <= r1:
            nums[l1],nums[r1] =nums[r1],nums[l1]
            l1+=1
            r1-=1
        r1 = len(nums)-1
        l = k
        while l <= r1:
            nums[l],nums[r1] =nums[r1],nums[l]
            r1-=1
            l+=1
        return nums
        

       
        



        
        

         
        
        

        """
        [0,0,0,0]
        """
        



  

       
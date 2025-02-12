class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k%len(nums)
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            my_index = (i+k) % len(nums)
            res[my_index]= nums[i]
        for i in range(len(nums)):
            nums[i] = res[i]
        

        """
        [0,0,0,0]
        """
        



  

       
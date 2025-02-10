class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0,0,0]
        for i in nums:
            count[i]+=1
        k=0
        for i in range(3):
            while count[i]>0:
                nums[k]=i
                k+=1
                count[i]-=1
              



    

        
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        res=[]

        for i in range(length):
            for j in range(length-i-1):
                if nums[j] > nums[j+1]:
                    nums[j] , nums[j+1] = nums[j+1] , nums[j]
                else:
                    continue
        i = 0
        while length > 0:
            if nums[i] == target:
                res.append(i)
                i+=1
                length-=1
            else:
                i+=1
                length-=1
        return res

 



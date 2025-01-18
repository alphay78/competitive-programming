class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r= len(nums)-1
        res=[]
        while l<=r:
            if abs(nums[l]) > abs(nums[r]):
                res.append(nums[l] ** 2)
                l+=1
            else:
                res.append(nums[r] ** 2)
                r-=1
                
        res.reverse()

        return res

        
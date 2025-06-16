class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        used = [False] * n
        res = []
        perm = []
    
        def backtrack():
            if len(perm) == n:
                res.append(perm.copy())
                return
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                perm.append(nums[i])
                backtrack()
                perm.pop()
                used[i] = False
    
        backtrack()
        return res
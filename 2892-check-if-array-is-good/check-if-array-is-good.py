
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)  

        if len(nums) != n + 1:
            return False
        
        expected = list(range(1, n)) + [n, n] 
        E=Counter(expected) 
        # nums.sort()  
        dict = Counter(nums)
        for k,v in dict.items():
            if E[k] != v:
                return False
        return True

        return nums == expected
        
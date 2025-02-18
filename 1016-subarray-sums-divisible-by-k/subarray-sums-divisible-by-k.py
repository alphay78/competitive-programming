class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        pre_sum = 0
        mod_count = {0:1}

        for i in nums:
            pre_sum+= i
            remainder = pre_sum % k 
            if remainder < 0:  
                remainder += k
            if remainder in mod_count: 
                res += mod_count[remainder]
            mod_count[remainder] = mod_count.get(remainder, 0) + 1
        return res
            
        
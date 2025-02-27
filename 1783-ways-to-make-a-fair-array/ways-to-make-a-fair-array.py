class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums) 
        even_presum = [0]*(n+1) 
        odd_presum = [0]*(n+1) 
        for i,num in enumerate(nums):
            if i % 2:
                odd_presum[i+1] = odd_presum[i] + num
                even_presum[i+1] = even_presum[i]
            else:
                even_presum[i+1] = even_presum[i] + num
                odd_presum[i+1] = odd_presum[i]
        ans = 0

        for i in range(1,n+1):
            odd_sum1 = odd_presum[i-1]
            even_sum1 = even_presum[i-1]

            odd_sum2 = even_presum[-1] - even_presum[i]
            even_sum2 = odd_presum[-1] - odd_presum[i]

            if odd_sum1 + odd_sum2 == even_sum1 + even_sum2:
                ans+=1
        return ans




        
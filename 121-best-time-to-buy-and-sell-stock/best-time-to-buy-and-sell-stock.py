class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min_profit=float("inf")
        max_profit=0

        for price in prices:
            if price < min_profit:
                min_profit = price

            elif price - min_profit > max_profit:
                max_profit = price - min_profit

        return max_profit


      
        

           



        
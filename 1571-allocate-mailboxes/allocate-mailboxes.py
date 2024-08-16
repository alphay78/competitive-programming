class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        """
            q. 
            
            
            it always make sense to put mail box in the middle most position
            now question remains, middle of how many houses.. since we need lookahead to find how many houses should be taken for current-i mailbox, we will dp this
            
            
            sequence bounded knapsack
            minimize house to mailbox distance
            
            dp(curr_house_i, prev_covered_house ,remaining_mailbox)
                states
            state transition
                1. but mail box here
                    currcost() + dp(curr_h, curr_h, rem-1)
                2. donot put mail here
                    dp(curr_house_i+1, prev_covered, remain)
                
                return min
                
                currcost() -> take current_i, prev_i and return cost 
                
            
            
            base case
                reached at end 
            
        """
        houses.sort()
        
        @cache
        def curr_cost(start_i, end_i):
            
            if start_i == end_i:
                return 0
            
            mid = houses[(end_i + start_i) // 2]
            
            diff = 0
            
            for i in range(start_i, end_i + 1):
                diff += abs(mid - houses[i])
            
            return diff
    
        @cache
        def dp(ci, pi, remains):
            
            if ci == len(houses):
                if ci == pi and remains == 0:
                    return 0
                else:
                    return inf
                
            if remains == 0:
                # cant place any more mailboxes
                return inf
            
            
            cost_place_here = curr_cost(pi, ci)
            
            return min(cost_place_here + dp(ci+1, ci+1, remains-1), dp(ci+1, pi, remains))
    
        
        return dp(0, 0, k)
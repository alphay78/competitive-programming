from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  
        l = 0  
        r = len(people) - 1  
        num_boats = 0  

        while l <= r:
            if people[l] + people[r] <= limit: 
                l += 1  
            r -= 1  
            num_boats += 1  

        return num_boats

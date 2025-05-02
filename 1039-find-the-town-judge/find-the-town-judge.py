from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustScore = [0] * (n + 1)

        for a, b in trust:
            trustScore[a] -= 1  
            trustScore[b] += 1  

        for person in range(1, n + 1):
            if trustScore[person] == n - 1:
                return person

        return -1 

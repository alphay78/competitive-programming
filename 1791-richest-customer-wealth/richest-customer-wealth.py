class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for i in accounts:
            if sum(i) > richest :
                richest = sum(i)
        return richest
        
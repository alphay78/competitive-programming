class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        potential_count = float('inf')
        d = {}
        
        # poor man's counter.
        for c in text:
            d[c] = d.get(c, 0) + 1
        
        # we need minimum count of b a n to be potential count
        for c in "ban":
            if d.get(c, 0) < potential_count:
                potential_count = d.get(c, 0)
        # if l and o are less than twice of potential_count, potential count is half of # of "l/o"s
        for c in "lo":
            if d.get(c, 0) < potential_count*2:
                potential_count = d.get(c,0)//2
        return potential_count
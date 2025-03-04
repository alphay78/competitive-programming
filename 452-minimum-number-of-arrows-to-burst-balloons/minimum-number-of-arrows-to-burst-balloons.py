
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        last_arrow = points[0][1] 
        for start, end in points:
            if start > last_arrow:
                arrows += 1
                last_arrow = end  
        return arrows

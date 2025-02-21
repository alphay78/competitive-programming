class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        a = 0
        b = 0
        m = len(firstList)
        n = len(secondList)
        while a < m and b<n:
            a1,a2 = firstList[a]
            b1,b2 = secondList[b]
            if b2 > a2:
                a += 1
            elif b2 < a2:
                b += 1
            else:
                a += 1
                b += 1
            if a1<=b2 and b1<=a2:
                result.append([max(a1,b1),min(a2,b2)])
        return result
        
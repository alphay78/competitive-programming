class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a,b = 0 , int(sqrt(c))
        while a <= b:
            square = a*a + b*b
            if square < c:
                a+=1
            elif square > c:
                b-=1
            else:
                return True
        return False



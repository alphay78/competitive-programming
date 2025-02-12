class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c)) + 1):
            b_square = c - a*a
            b = int(math.sqrt(b_square))

            if b_square == b*b:
                return True
        return False
        
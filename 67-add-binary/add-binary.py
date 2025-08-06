class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)

        while y != 0:
            sum_without_carry = x ^ y
            carry = (x & y) << 1
            x, y = sum_without_carry, carry
        
        return bin(x)[2:]

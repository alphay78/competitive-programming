class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        return ''.join(reversed(result))

# Instantiate the class
solution = Solution()

# Test cases
print(solution.convertToTitle(1))   # Output: "A"
print(solution.convertToTitle(28))  # Output: "AB"
print(solution.convertToTitle(701)) # Output: "ZY"

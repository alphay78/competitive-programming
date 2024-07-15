class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            result = result * 26 + (ord(char) - ord('A') + 1)
        return result

# Example usage:
solution = Solution()
print(solution.titleToNumber("A"))   # Output: 1
print(solution.titleToNumber("B"))   # Output: 2
print(solution.titleToNumber("Z"))   # Output: 26
print(solution.titleToNumber("AA"))  # Output: 27
print(solution.titleToNumber("AB"))  # Output: 28

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()  # Split the input string into individual words
        if words:  # Check if there are any words
            last_word = words[-1]  # Get the last word
            return len(last_word)  # Return the length of the last word
        else:
            return 0  # If no words, return 0

# Example usage
solution = Solution()
result = solution.lengthOfLastWord("I love You")
print(result)  # Output: 3 (length of "You"))
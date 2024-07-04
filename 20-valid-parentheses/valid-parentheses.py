class Solution(object):
    def isValid(self, s):
        # Stack to keep track of opening brackets
        stack = []
        
        # Dictionary to keep mappings of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate over each character in the string
        for char in s:
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for this closing bracket doesn't match the stack's top element, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)
        
        # If the stack is empty, all the opening brackets have been closed
        return not stack

# Example usage:
solution = Solution()
print(solution.isValid("()"))       # Output: True
print(solution.isValid("()[]{}"))   # Output: True
print(solution.isValid("(]"))       # Output: False

class Solution:
    def interpret(self, command):
        return command.replace("()", "o").replace("(al)", "al")

# Example usage
command = "G()(al)"
solution = Solution()
interpreted_command = solution.interpret(command)
print(interpreted_command)
                 

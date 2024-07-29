class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        def next_term(term: str) -> str:
            result = []
            i = 0
            while i < len(term):
                count = 1
                while i + 1 < len(term) and term[i] == term[i + 1]:
                    i += 1
                    count += 1
                result.append(str(count) + term[i])
                i += 1
            return "".join(result)
        
        current_term = "1"
        for _ in range(2, n + 1):
            current_term = next_term(current_term)
        
        return current_term

# Example usage:
solution = Solution()
print(solution.countAndSay(4))  # Output: "1211"
print(solution.countAndSay(1))  # Output: "1"

class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
            
        for i in range(len(s)):
            # Check if there's a next character and if the current character is less than the next
            if i < len(s) - 1 and dic[s[i]] < dic[s[i + 1]]:
                sum -= dic[s[i]]  # Subtract current value
            else:
                sum += dic[s[i]]  # Add current value
        
        return sum
            
            

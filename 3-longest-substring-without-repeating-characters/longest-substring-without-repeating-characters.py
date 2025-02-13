class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = {} 
        left = 0  
        max_length = 0  
        
        for r in range(len(s)):
            if s[r] in my_dict and my_dict[s[r]] >= left:
                left = my_dict[s[r]] + 1  
            
            my_dict[s[r]] = r 
            max_length = max(max_length, r - left + 1)  
        
        return max_length

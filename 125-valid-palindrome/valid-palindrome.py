class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''.join(character for character in s if character.isalnum()).lower()
        
        l = 0
        r = len(x) - 1
        
        while l < r:
            if x[l] != x[r]:
                return False
            r -= 1
            l += 1
        return True





                
        


        
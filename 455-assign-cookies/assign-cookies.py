class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
         g.sort()  # Sort the greed factors
         s.sort()  # Sort the cookie sizes
    
         child_i = 0  # Pointer for children
         cookie_j = 0  # Pointer for cookies
    
         while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                # If the current cookie can satisfy the current child
                child_i += 1  # Move to the next child
            cookie_j += 1  # Move to the next cookie
            
         return child_i  # Number of content children
                
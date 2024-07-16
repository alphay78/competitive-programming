class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Check if the lengths of both strings are equal
        if len(s) != len(t):
            return False

        # Dictionary to store the mapping from characters in s to t
        mapping_s_to_t = {}
        # Dictionary to store the mapping from characters in t to s
        mapping_t_to_s = {}

        # Iterate through the characters of both strings
        for char_s, char_t in zip(s, t):
            # Check if there is a previous mapping for char_s
            if char_s in mapping_s_to_t:
                # If the previous mapping does not match char_t, return False
                if mapping_s_to_t[char_s] != char_t:
                    return False
            else:
                # If char_s is not in the dictionary, add the mapping
                mapping_s_to_t[char_s] = char_t

            # Check if there is a previous mapping for char_t
            if char_t in mapping_t_to_s:
                # If the previous mapping does not match char_s, return False
                if mapping_t_to_s[char_t] != char_s:
                    return False
            else:
                # If char_t is not in the dictionary, add the mapping
                mapping_t_to_s[char_t] = char_s

        # If all characters have been checked and mappings are consistent, return True
        return True

# Test cases
solution = Solution()
print(solution.isIsomorphic("egg", "add"))  # Output: True
print(solution.isIsomorphic("foo", "bar"))  # Output: False
print(solution.isIsomorphic("paper", "title"))  # Output: True

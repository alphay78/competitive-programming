class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 :
            return ""

        x=""
        min_length=min(len(i) for i in strs )

        for i in range(min_length):
            char= strs[0][i]
            if all(char==s[i] for s in strs):
                x+=char
            else:
                break
        return x
        

        
        

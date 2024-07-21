class Solution:
    def reverseVowels(self, s: str) -> str:
        c = []
        v = []
        r = ''
        vowels = set(["i", "e", "a", "o", "u", "A", "E", "I", "O", "U"])
        backpointer = len(s)
        for i in range(len(s)):
            if s[i] in vowels:
                backpointer -= 1
                while s[backpointer] not in vowels:
                    backpointer -= 1
                r += s[backpointer]
            else:
                r += s[i]
        return r
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        track = [0 for i in range(len(s)+1)]

        for left,right,direction in shifts:
            if direction == 1:
                track[left] += 1
                track[right+1] -= 1
            else:
                track[left] -= 1
                track[right +1] += 1
        for i in range(1,len(track)):
            track[i] += track[i-1]
        res = []
        for i,j in enumerate(s):
            t = ord(j) - 97
            letter =  (t + track[i])%26
            letter = chr(letter+97)
            res.append(letter)
        return "".join(res)
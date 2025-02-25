class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        pre = 0
        track = {0:1}
        ans = 0
        for i in arr:
            pre+=i
            temp = pre%2
            ans += track.get(temp,0)
            track[temp] = track.get(temp,0) + 1
        n = len(arr)
        x =( (n+1)*n)//2
        y = x - ans
        return y%(10**9 +7)


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic_p=Counter(p)
        dic_s = defaultdict(int)
        l=0
        res=[]
        for i in range(len(s)):
            dic_s[s[i]] += 1
            while i-l+1 > len(p):
                dic_s[s[l]]-=1
                if dic_s[s[l]] <=0:
                    del dic_s[s[l]]

                l += 1
            if dic_s == dic_p:
                res.append(l)
        return res
            

            















       ## while l<r:
       ##     dic1=Counter([0,len(s)])
        ##    if dic==dic1:
       ##         res.append(i)
           ##  l+=1 
           ##  r+=1 
      ##  return res
                
                

         
            

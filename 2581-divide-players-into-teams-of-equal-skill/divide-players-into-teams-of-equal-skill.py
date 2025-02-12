class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l=0
        r=len(skill)-1
        pre = skill[l] + skill[r]
        res = 0
        while l<r:
            s = skill[l] +skill[r]
            if pre == s:
                m = skill[l]*skill[r]
                res+=m
                l+=1
                r-=1
            else:
                return -1
                
        return res




            

  

                 

                 

               
            
            




            

   
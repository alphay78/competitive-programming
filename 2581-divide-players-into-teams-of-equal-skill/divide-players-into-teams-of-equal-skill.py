class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill=sorted(skill)
        l=0
        r=len(skill)-1
        s=skill[l]+skill[r]
        res=0
        for i in range (len(skill)//2):
            if skill[l]+skill[r]!=s:
                return -1
            else:
                res+=skill[l]*skill[r]
            l+=1
            r-=1
        return res
                    

                 

                 

               
            
            




            

   
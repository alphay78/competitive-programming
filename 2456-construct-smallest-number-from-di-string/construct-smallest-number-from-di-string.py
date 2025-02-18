class Solution:
    def smallestNumber(self, p: str) -> str: 
        return ''.join(map(str,reduce(lambda a,i:a+[*range(i,len(a),-1)],(i for i,c in enumerate(p+'I',1) if c=='I'),[])))
        
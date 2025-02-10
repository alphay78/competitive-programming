class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        max_height = max(heights)
        count = [[] for i in range(max_height+1)]

        for i in range(len(heights)):
            count[heights[i]].append(names[i])

        sorted_names = []

        for height in range(max_height,-1,-1):
            sorted_names.extend(count[height])
        return sorted_names



      

       



        

    
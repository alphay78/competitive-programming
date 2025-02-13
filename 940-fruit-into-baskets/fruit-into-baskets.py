class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        my_dict = defaultdict(int)
        l = 0
        total = 0
        count = 0
        for r in range(len(fruits)):
            my_dict[fruits[r]]+=1
            total+=1
            while len(my_dict) > 2:
                total-=1
                my_dict[fruits[l]]-=1
                if my_dict[fruits[l]] == 0:
                    del my_dict[fruits[l]]
                l+=1
            count = max(count,total)
        return count

    

        
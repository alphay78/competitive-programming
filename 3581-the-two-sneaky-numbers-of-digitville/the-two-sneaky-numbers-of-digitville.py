class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        my_dict = Counter(nums)
        my_list =[]

        for i,j in my_dict.items():
            if j == 1:
                continue
            else:
                my_list.append(i)

        return my_list




        
class Solution(object):
    def findDuplicates(self, nums):
        dict={}
        New_list=[]

        for i in nums:
            if i in dict:
                New_list.append(i)
            else:
                dict[i]=1
        return set(New_list)

        
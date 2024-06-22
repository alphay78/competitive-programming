class Solution(object):
    def intersection(self, nums1, nums2):
       dict={}
       New_list=[]
       for i in nums1:
            if i in dict:
                continue
            else: 
                dict[i]=1
     
       for j in nums2:
            if j in dict:
                New_list.append(j)
            else:
                continue
        
       return set(New_list)

        
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        New_list=[]
        for i in nums1:
            for j in nums2:
                if i == j :
                    New_list.append(i)
                else: 
                    continue
        return set(New_list)
class Solution(object):
    def intersection(self, nums1, nums2):
        mydict = {}

        for num in nums1:
            if (num in nums2) and (num not in mydict.keys()):
                mydict[num] = num
        return list(set(mydict.keys()))
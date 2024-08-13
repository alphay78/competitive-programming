# from typing import List
# from collections import Counter

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        dict_target = Counter(target)
        dict_arr = Counter(arr)

        return dict_target == dict_arr



        
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
         sorted_target = sorted(target)
         sorted_arr = sorted(arr)
    
         return sorted_target == sorted_arr


        
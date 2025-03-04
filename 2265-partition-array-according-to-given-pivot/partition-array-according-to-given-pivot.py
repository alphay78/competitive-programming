class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_pivot = []
        equal_pivot = []
        great_pivot = []

        for i in range(len(nums)):
            if nums[i] < pivot:
                less_pivot.append(nums[i])
            elif nums[i] > pivot:
                great_pivot.append(nums[i])
            else:
                equal_pivot.append(nums[i])
        return less_pivot + equal_pivot + great_pivot
        
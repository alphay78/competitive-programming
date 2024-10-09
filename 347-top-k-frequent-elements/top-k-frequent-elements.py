
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)  # Get frequency of each number
        # Sort the keys of count by their frequency in descending order and get the top k
        return [num for num, freq in count.most_common(k)]

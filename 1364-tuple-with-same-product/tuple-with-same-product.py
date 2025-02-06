class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        my_dict = defaultdict(int)
        
        # Generate product pairs
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):  # Avoid redundant pairs
                product = nums[i] * nums[j]
                my_dict[product] += 1  # Count occurrences of each product

        count = 0
        for val in my_dict.values():
            if val > 1:
                count += val * (val - 1) * 4  # Formula for valid tuples
                
        return count

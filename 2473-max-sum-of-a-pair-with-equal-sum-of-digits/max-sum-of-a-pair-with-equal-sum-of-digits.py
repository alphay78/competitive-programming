class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_map = defaultdict(list)  
        max_sum = -1 
        
        # Function to calculate the sum of digits of a number
        def digitSum(num):
            return sum(int(digit) for digit in str(num))
    
        # Group numbers by their digit sum
        for num in nums:
            key = digitSum(num)
            digit_sum_map[key].append(num)
        
        # Find the maximum sum of two numbers with the same digit sum
        for key, values in digit_sum_map.items():
            if len(values) > 1:
                values.sort(reverse=True)  # Sort to get the two largest numbers
                max_sum = max(max_sum, values[0] + values[1])
        
        return max_sum

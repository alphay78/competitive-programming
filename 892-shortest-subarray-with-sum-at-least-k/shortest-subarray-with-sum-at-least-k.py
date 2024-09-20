from collections import deque

class Solution:
    def shortestSubarray(self, nums, k):
        # Calculate prefix sums
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # Deque to store indices of prefix sums
        dq = deque()
        min_len = float('inf')  # Initialize with infinity (no subarray found yet)
        
        for i in range(n + 1):
            # Check if we can form a valid subarray
            while dq and prefix_sum[i] - prefix_sum[dq[0]] >= k:
                min_len = min(min_len, i - dq.popleft())
            
            # Ensure the deque elements are increasing by prefix_sum values
            while dq and prefix_sum[i] <= prefix_sum[dq[-1]]:
                dq.pop()
            
            # Add the current index to the deque
            dq.append(i)
        
        return min_len if min_len != float('inf') else -1

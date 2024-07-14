class Solution:
    # Definition for a binary tree node.
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def sortedArrayToBST(self, nums):
        # Helper function to convert array to BST
        def convert(left, right):
            if left > right:
                return None

            # Always choose middle element to ensure balance
            mid = (left + right) // 2

            # Create a new tree node with the middle element
            node = Solution.TreeNode(nums[mid])

            # Recursively construct the left and right subtrees
            node.left = convert(left, mid - 1)
            node.right = convert(mid + 1, right)

            return node

        # Start the recursive process
        return convert(0, len(nums) - 1)

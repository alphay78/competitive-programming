# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def height(node):
            if not node:
                return 0  # Base case: empty subtree

            left = height(node.left)
            if left == -1:
                return -1  # Left subtree not balanced

            right = height(node.right)
            if right == -1:
                return -1  # Right subtree not balanced

            if abs(left - right) > 1:
                return -1  # Current node not balanced

            return 1 + max(left, right)  # Height of current node

        return height(root) != -1
        
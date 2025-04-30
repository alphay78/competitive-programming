# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        
        def dfs(leftChild, rightChild, level):
            if not leftChild and not rightChild:
                return

            if level % 2 == 1:
                leftChild.val, rightChild.val = rightChild.val, leftChild.val

            dfs(leftChild.left, rightChild.right, level + 1)
            dfs(leftChild.right, rightChild.left, level + 1)

        dfs(root.left, root.right, 1)

        return root

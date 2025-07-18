# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        def dfs(node, currSum):
            if not node:
                return False
            currSum += node.val

            if not node.left and not node.right:
                return currSum == targetSum
            return dfs(node.left , currSum) or dfs(node.right , currSum)

        return dfs(root , 0)







     
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        res = []  
        def dfs(node, currSum, path):
            if not node:
                return
            currSum += node.val
            path.append(node.val)

            if not node.left and not node.right:
                if currSum == targetSum:
                    res.append(list(path))  
            dfs(node.left, currSum, path)
            dfs(node.right, currSum, path)

            path.pop()

        dfs(root, 0, [])
        return res

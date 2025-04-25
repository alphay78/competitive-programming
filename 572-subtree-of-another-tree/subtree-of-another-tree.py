# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root, subRoot):
            if not root and not subRoot:
                return True
            if (root and not subRoot) or (not root and subRoot):
                return False

            if root.val != subRoot.val:
                return False
            
            return helper(root.left, subRoot.left) and helper(root.right, subRoot.right)
            

        def check(root):
            if not root:
                return False

            if helper(root, subRoot):
                return True
            return check(root.left) or check(root.right)

        return check(root)

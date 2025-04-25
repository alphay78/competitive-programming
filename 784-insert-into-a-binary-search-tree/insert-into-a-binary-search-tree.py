# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:  # If the root is None, create a new node and return it.
            return TreeNode(val)

        # If the value is smaller, go to the left subtree.
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        # If the value is larger, go to the right subtree.
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        # Return the root node after the insertion is done.
        return root
        
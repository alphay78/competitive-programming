# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        arr = []
        dummy = root
        def run_tree(node, tmp):
            if node is None:
                return
            if node.left == None and node.right == None:
                tmp = tmp + str(node.val)
                arr.append(int(tmp))
                return
            tmp = tmp + str(node.val)
            run_tree(node.left, tmp)
            run_tree(node.right, tmp)
        run_tree(dummy, "")
        return sum(arr)

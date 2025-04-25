# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            result = []
            def dfs(node):
                if not node:
                    return
                dfs(node.left)         # Step 1: Go Left
                result.append(node.val)  # Step 2: Visit Node
                dfs(node.right)        # Step 3: Go Right

            dfs(root)
            return result

        
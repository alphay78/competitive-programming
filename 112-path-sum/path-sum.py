class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        # If it's a leaf node, check if the path sum equals targetSum
        if not root.left and not root.right:
            return root.val == targetSum
        
        # Recursively check left and right subtrees with updated sum
        remainingSum = targetSum - root.val
        return (
            self.hasPathSum(root.left, remainingSum) or
            self.hasPathSum(root.right, remainingSum)
        )

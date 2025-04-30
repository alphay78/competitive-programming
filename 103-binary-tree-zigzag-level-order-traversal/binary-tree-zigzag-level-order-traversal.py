# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root]) 
        result = []
        left_to_right = True

        while queue:
            level_of_node = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_of_node.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                level_of_node.reverse()
            
            result.append(level_of_node)
            left_to_right = not left_to_right
        
        return result

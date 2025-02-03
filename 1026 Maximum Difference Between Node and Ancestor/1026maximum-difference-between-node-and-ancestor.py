# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode], curr_max: int, curr_min: int) -> None:
            if not node:
                return
            
            new_max = max(curr_max, node.val)
            new_min = min(curr_min, node.val)
            
            self.answer = max(self.answer, abs(new_max - new_min))

            if node.left:
                dfs(node.left, new_max, new_min)

            if node.right:
                dfs(node.right, new_max, new_min)
            
            
        dfs(root, root.val, root.val)
        return self.answer

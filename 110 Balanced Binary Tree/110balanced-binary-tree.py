# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            return 1 + max(height(node.left), height(node.right))

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True

            return (
                abs(height(node.left) - height(node.right)) <= 1 
                and self.isBalanced(node.left) 
                and self.isBalanced(node.right)
            )

        return dfs(root)
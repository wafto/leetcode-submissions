# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.answer = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left = 0 if not node.left else dfs(node.left) + 1
            right = 0 if not node.right else dfs(node.right) + 1 

            self.answer = max(self.answer, left + right)

            return max(left, right)

        dfs(root)
        return self.answer

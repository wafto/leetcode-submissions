# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            return 1 + max(depth(node.left), depth(node.right))
        
        def balanced(node: Optional[TreeNode]) -> bool:
            if not node:
                return True

            if not node.left and not node.right:
                return True

            if abs(depth(node.left) - depth(node.right)) > 1:
                return False

            return balanced(node.left) and balanced(node.right)

        return balanced(root)

            

            
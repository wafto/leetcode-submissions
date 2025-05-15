# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def same(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return True

            if not a or not b:
                return False

            return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)

        if not subRoot:
            return True

        if not root:
            return False

        def subtree(node: Optional[TreeNode]) -> bool:
            if not node:
                return False

            if node.val == subRoot.val and same(node, subRoot):
                return True

            return subtree(node.left) or subtree(node.right)

        return subtree(root)


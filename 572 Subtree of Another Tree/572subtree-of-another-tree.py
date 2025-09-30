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

        queue = deque([root])

        while queue:
            node = queue.popleft()

            if same(node, subRoot):
                return True

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return False

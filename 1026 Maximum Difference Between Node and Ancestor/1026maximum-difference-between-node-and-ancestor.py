# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node: Optional[TreeNode], curr_max: int, curr_min: int) -> None:
            if not node:
                return
            
            self.ans = max(self.ans, abs(curr_max - curr_min))

            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)

            if node.left:
                dfs(node.left, max(curr_max, node.left.val), min(curr_min, node.left.val))

            if node.right:
                dfs(node.right, max(curr_max, node.right.val), min(curr_min, node.right.val))

        dfs(root, root.val, root.val)

        return self.ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node: TreeNode, maxInPath: int) -> int:
            if not node:
                return 0

            maxCurr = max(node.val, maxInPath)

            total = 1 if maxCurr == node.val else 0
            total += dfs(node.left, maxCurr)
            total += dfs(node.right, maxCurr)

            return total

        return dfs(root, float(-inf))
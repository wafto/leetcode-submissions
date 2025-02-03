# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        queue = deque([root])
        ans = 0

        while queue:
            node = queue.popleft()
            if low <= node.val <= high:
                ans += node.val
            if node.left and node.val > low:
                queue.append(node.left)
            if node.right and node.val < high:
                queue.append(node.right)

        return ans

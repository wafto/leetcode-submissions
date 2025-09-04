# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        queue = deque()

        if not root:
            return total

        queue.append(root)

        while queue:
            node = queue.popleft()

            if low <= node.val <= high:
                total += node.val

            if node.left and node.val > low:
                queue.append(node.left)  

            if node.right and node.val < high:
                queue.append(node.right)

        return total
    
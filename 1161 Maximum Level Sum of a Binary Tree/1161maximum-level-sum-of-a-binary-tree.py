# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maximal_sum = float(-inf)
        maximal_level = 0
        levels = 0

        queue = deque()
        queue.append(root)

        while queue:
            current_sum = 0
            levels += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                current_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if current_sum > maximal_sum:
                maximal_sum = current_sum
                maximal_level = levels

        return maximal_level
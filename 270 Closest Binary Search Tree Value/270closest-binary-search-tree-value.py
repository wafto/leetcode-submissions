# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = float('inf')
        cnode = None
        queue = deque([root])

        while queue:
            node = queue.popleft()
            diff = abs(node.val - target)

            if diff == closest:
                cnode = cnode if cnode.val < node.val else node 

            if diff < closest:
                closest = diff
                cnode = node
    
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return cnode.val if cnode else root.val
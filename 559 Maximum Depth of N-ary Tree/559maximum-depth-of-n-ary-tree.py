"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(node, depth):
            if not node:
                return 0

            if not node.children:
                return 1

            largest = 0
            for child in node.children:
                largest = max(largest, dfs(child, depth))

            return largest + 1

        return dfs(root, 0)

            
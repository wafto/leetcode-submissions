# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        hashmap = defaultdict(list)
        levels = []

        def dfs(node: Optional[TreeNode], level: int) -> int:
            if not node:
                return level
            hashmap[level].append(node.val)
            return max(dfs(node.left, level + 1), dfs(node.right, level + 1))

        maxlevel = dfs(root, 0)

        for i in range(maxlevel):
            levels.append(hashmap[i])

        return levels

            



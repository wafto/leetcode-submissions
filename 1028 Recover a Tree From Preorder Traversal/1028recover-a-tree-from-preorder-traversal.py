# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        depth, queue, n = 0, deque(), len(traversal)

        i = 0
        while i < n:
            if traversal[i] == '-':
                depth += 1
                i += 1
            else:
                j = i
                while j < n and traversal[j].isdigit():
                    j += 1
                queue.append((depth, int(traversal[i: j])))
                depth, i = 0, j

        def dfs(depth: int) -> Optional[TreeNode]:
            if not queue or queue[0][0] != depth:
                return None
            
            _, val = queue.popleft()

            node = TreeNode(val)
            node.left = dfs(depth + 1)
            node.right = dfs(depth + 1)

            return node

        return dfs(0)
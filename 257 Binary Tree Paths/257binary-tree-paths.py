# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []

        def dfs(node: Optional[TreeNode], curr: List[str]) -> None:
            if not node:
                return

            if not node.left and not node.right:
                copy = curr.copy()
                copy.append(str(node.val))
                answer.append('->'.join(copy))
                return 
            
            curr.append(str(node.val))
            dfs(node.left, curr)
            dfs(node.right, curr)
            curr.pop()

        dfs(root, [])
        return answer
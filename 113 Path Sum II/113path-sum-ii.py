# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []

        def backtracking(node: Optional[TreeNode], curr: List[int], acc: int) -> None:
            if not node:
                return

            curr.append(node.val)
            acc += node.val

            if not node.left and not node.right and acc == targetSum:
                ans.append(curr.copy())
            else:
                backtracking(node.left, curr, acc)
                backtracking(node.right, curr, acc)

            curr.pop()

        backtracking(root, [], 0)
        return ans

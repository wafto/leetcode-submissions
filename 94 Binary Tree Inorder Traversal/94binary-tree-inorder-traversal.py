# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []
        stack = []

        curr = root
       
        while curr:
            stack.append(curr)
            curr = curr.left

        while stack:
            node = stack.pop()
            traversal.append(node.val)
            curr = node.right
            while curr:
                stack.append(curr)
                curr = curr.left

        return traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        curr = root

        while curr:
            currdiff = abs(curr.val - target)
            closestdiff = abs(closest - target)

            if currdiff < closestdiff:
                closest = curr.val
            elif currdiff == closestdiff and curr.val < closest:
                closest = curr.val

            if target < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        return closest

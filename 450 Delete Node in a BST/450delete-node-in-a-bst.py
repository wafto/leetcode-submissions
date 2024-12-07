# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minValueNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root
        while current and current.left:
            current = current.left
        return current

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        minNode = self.minValueNode(root.right)
        root.val = minNode.val
        root.right = self.deleteNode(root.right, minNode.val)
        return root
        
        
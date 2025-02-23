# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        postindexes = {n: i for i, n in enumerate(postorder)}

        def build(i1: int, i2: int, j1: int, j2: int) -> Optional[TreeNode]:
            if i1 > i2 or j1 > j2:
                return None

            root = TreeNode(preorder[i1])

            if i1 != i2:
                pos = postindexes[preorder[i1 + 1]]
                size = pos - j1 + 1
                root.left = build(i1 + 1, i1 + size, j1, pos)
                root.right = build(i1 + 1 + size, i2, pos + 1, j2 - 1)
            
            return root

        return build(0, n - 1, 0, n - 1)
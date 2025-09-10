# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        answer = []
        hashmap = defaultdict(int)

        def dfs(node):
            if not node:
                return '_'
            
            key = f'{str(node.val)}#{dfs(node.left)}#{dfs(node.right)}'

            hashmap[key] += 1

            if hashmap[key] == 2:
                answer.append(node)

            return key

        dfs(root)

        return answer
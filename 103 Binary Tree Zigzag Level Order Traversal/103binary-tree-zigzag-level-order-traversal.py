# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level = 0
        queue = deque([root])
        answer = []

        while queue:
            level += 1
            curr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            
         
            answer.append(curr if level & 1 else curr[::-1])

        return answer


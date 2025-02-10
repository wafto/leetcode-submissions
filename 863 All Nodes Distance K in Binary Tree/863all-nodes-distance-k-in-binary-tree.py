# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        queue = deque([root])

        while queue:
            node = queue.popleft()
            
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                queue.append(node.left)
            
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                queue.append(node.right)
        
        queue = deque([target.val])
        seen = {target.val}
        distance = 0
        
        while queue:
            if distance == k:
                break
            
            for _ in range(len(queue)):
                node = queue.popleft()
                for nei in graph[node]:
                    if nei not in seen:
                        queue.append(nei)
                        seen.add(nei)
            
            distance += 1

        return list(queue)



        


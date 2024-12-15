"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = set()
        adjlist = dict()
        queue = deque()
        head = None

        visited.add(node.val)
        queue.append(node)
        
        while queue:
            for _ in range(len(queue)):
                v = queue.popleft()
               
                if v.val not in adjlist:
                    adjlist[v.val] = []
                
                for n in v.neighbors:
                    adjlist[v.val].append(n.val)
                    if n.val not in visited:
                        visited.add(n.val)
                        queue.append(n)

        mapping = dict()
        
        for key in adjlist:
            if key not in mapping:
                mapping[key] = Node(key)

            if not head:
                head = mapping[key]

            for n in adjlist[key]:
                if n not in mapping:
                    mapping[n] = Node(n)
                mapping[key].neighbors.append(mapping[n])
                
        return head







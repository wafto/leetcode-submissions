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

        graph = defaultdict(list)
        queue = deque([node])
        visited = set([node])

        while queue:
            node = queue.popleft()

            if node.val not in graph:
                graph[node.val] = []
            
            for child in node.neighbors:
                graph[node.val].append(child.val)
                if child in visited:
                    continue
                visited.add(child)
                queue.append(child)

        nodes = {i: Node(i) for i in range(1, len(graph) + 1)}

        for node in nodes.values():
            for child in graph[node.val]:
                node.neighbors.append(nodes[child])

        return nodes[1] if nodes else None


        
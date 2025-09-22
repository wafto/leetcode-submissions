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
        graph = {}

        def dfs(node, seen = set()):
            if not node or node.val in seen:
                return

            graph[node.val] = []
            seen.add(node.val)

            for neighbor in node.neighbors:
                graph[node.val].append(neighbor.val)
                dfs(neighbor, seen)

        dfs(node)

        copy = {key: Node(key) for key in graph.keys()}
        head = None

        for key in copy.keys():
            if head is None:
                head = copy[key]
            copy[key].neighbors = [copy[nkey] for nkey in graph[key]]

        return head
                


            

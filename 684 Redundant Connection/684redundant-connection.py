class DisjointSets:
    def __init__(self, n: int):
        self.dj = {i: i for i in range(1, n + 1)}

    def find(self, node: int) -> int:
        if self.dj[node] != node:
            self.dj[node] = self.find(self.dj[node])
        return self.dj[node]

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return  False

        self.dj[p1] = p2
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = len(edges)
        disjointset = DisjointSets(nodes)

        for n1, n2 in edges:
            if not disjointset.union(n1, n2):
                return [n1, n2]

        return []
    
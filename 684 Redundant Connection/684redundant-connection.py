class UnionFind:
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, n: int) -> int:
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]] # O(n) -> O(logn)
            p = self.parent[p]
        return p

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False # We have a cycle

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = self.parent[p1]
        elif self.rank[p2] > self.rank[p1]:
            self.parent[p1] = self.parent[p2]
        else:
            self.parent[p2] = self.parent[p1]
            self.rank[p1] += 1
        
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = len(edges)
        uf = UnionFind(nodes)

        for n1, n2 in edges:
            if not uf.union(n1, n2):
                return [n1, n2]

        return []
    
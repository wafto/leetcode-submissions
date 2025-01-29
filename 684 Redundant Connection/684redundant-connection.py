class UnionFind:
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n: int) -> int:
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True
    

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unionFind = UnionFind(len(edges))

        for n1, n2 in edges:
            if not unionFind.union(n1, n2):
                return [n1, n2]

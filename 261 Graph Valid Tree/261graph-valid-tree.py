class UnionFind:
    def __init__(self, n: int):
        self.par = {i: i for i in range(n)}
        self.rank = {i: 0 for i in range(n)}

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
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ufind = UnionFind(n)
        count = n

        for n1, n2 in edges:
            if not ufind.union(n1, n2):
                return False
            else:
                count -= 1

        return count == 1
        
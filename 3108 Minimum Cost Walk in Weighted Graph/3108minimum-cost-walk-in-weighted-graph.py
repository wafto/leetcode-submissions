class UnionFind:
    def __init__(self, n: int):
        self.parent = {}
        self.rank = {}
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, n: int) -> int:
        p = self.parent[n]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    
    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        return True

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        union_find = UnionFind(n)

        for u, v, _ in edges:
            union_find.union(u, v)

        cost = {}
        for u, v, w in edges:
            root = union_find.find(u)

            if root not in cost:
                cost[root] = w
            else:
                cost[root] &= w

        ans = []
        for src, dst in query:
            p1, p2 = union_find.find(src), union_find.find(dst)
            if p1 != p2:
                ans.append(-1)
            else:
                ans.append(cost[p1])

        return ans

            


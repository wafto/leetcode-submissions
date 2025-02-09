class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        routes, seen = set(), set()

        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            routes.add((x, y))

        def dfs(node: int) -> int:
            ans = 0
            for nei in graph[node]:
                if nei not in seen:
                    if (node, nei) in routes:
                        ans += 1
                    seen.add(nei)
                    ans += dfs(nei)
            return ans

        seen.add(0)
        return dfs(0)
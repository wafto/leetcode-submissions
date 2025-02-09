class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()

        def dfs(node: int) -> int:
            ans = 0
            if node not in graph:
                seen.add(node)
                return 1
            for nei in graph[node]:
                if nei not in seen:
                    ans = 1
                    seen.add(nei)
                    dfs(nei)
            return ans
        
        components = 0
        
        for i in range(n):
            components += dfs(i)

        return components

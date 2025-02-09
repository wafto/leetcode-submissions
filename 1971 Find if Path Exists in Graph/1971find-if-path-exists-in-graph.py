class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = {source}
        
        def dfs(node) -> bool:
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    if dfs(nei):
                        return True
            return False

        return dfs(source)



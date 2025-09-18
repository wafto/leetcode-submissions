class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        nodes = len(graph)
        colors = [-1] * nodes

        def dfs(node: int, curr: int, nxt: int) -> bool: 
            if colors[node] != -1:
                return colors[node] == curr

            colors[node] = curr

            for nei in graph[node]:
                if colors[nei] == -1 and not dfs(nei, nxt, curr):
                    return False
                elif colors[nei] != nxt:
                    return False

            return True

        for node in range(nodes):
            if colors[node] == -1 and not dfs(node, 0, 1):
                return False

        return True



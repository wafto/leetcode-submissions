class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)
        seen = set()

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        def dfs(node: int) -> None:
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        ans = 0
        for node in range(n):
            if node not in seen:
                ans += 1
                seen.add(node)
                dfs(node)

        return ans

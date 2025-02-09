class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = set()
        restricted = set(restricted)

        def dfs(node: int) -> None:
            if node in restricted:
                return
            for nei in graph[node]:
                if nei in seen or nei in restricted:
                    continue
                seen.add(nei)
                dfs(nei)
        
        seen.add(0)
        dfs(0)

        return len(seen)

            
                
                
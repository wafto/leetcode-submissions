class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        dst = len(graph) - 1

        def backtracking(curr: List[int]) -> None:
            if curr[-1] == dst:
                paths.append(curr.copy())
                return
            
            for nei in graph[curr[-1]]:
                curr.append(nei)
                backtracking(curr)
                curr.pop()

        backtracking([0])
        return paths

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = {}

        def isSafe(v: int) -> bool:
            if v in safe:
                return safe[v]
            # assume false to detect cycles
            safe[v] = False
            for rel in graph[v]:
                if not isSafe(rel):
                    return safe[v]
            safe[v] = True
            return safe[v]
            
        ans = []
        for i in range(len(graph)):
            if isSafe(i):
                ans.append(i)
        return ans
        
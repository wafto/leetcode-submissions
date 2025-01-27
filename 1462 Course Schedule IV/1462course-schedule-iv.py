class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {n: [] for n in range(numCourses)}
        mapping = {}
 
        for pre, course in prerequisites:
            adj[course].append(pre)

        def dfs(course: int) -> None:
            if course not in mapping:
                mapping[course] = set()
                for pre in adj[course]:
                    mapping[course] |= dfs(pre)
                mapping[course].add(course)
            return mapping[course]

        for course in range(numCourses):
            dfs(course)

        ans = []
        for u, v in queries:
            ans.append(u in mapping[v])

        return ans
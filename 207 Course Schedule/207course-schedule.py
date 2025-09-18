class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)

        def dfs(course: int, seen: Set[int]) -> bool:
            if course in seen:
                return False

            if not graph[course]:
                return True

            seen.add(course)

            for prereq in graph[course]:
                if not dfs(prereq, seen):
                    return False

            seen.remove(course)
            graph[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course, set()):
                return False

        return True

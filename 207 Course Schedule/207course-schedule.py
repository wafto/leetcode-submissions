class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        def dfs(course: int, seen: Set[int]) -> bool:
            if course in seen:
                return False

            if not graph[course]:
                return True

            seen.add(course)

            for neighbor in graph[course]:
                if not dfs(neighbor, seen):
                    return False

            seen.remove(course)
            graph[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course, set()):
                return False

        return True



            

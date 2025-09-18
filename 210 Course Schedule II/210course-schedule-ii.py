class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        answer = []
        path = set()
        seen = set()

        def dfs(course: int) -> bool:
            if course in path:
                return False

            if course in seen:
                return True

            seen.add(course)
            path.add(course)

            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False

            path.remove(course)
            answer.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return answer
        

            
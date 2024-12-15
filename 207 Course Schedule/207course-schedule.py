class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapping = {n:[] for n in range(numCourses)}

        for course, pre in prerequisites:
            mapping[course].append(pre)

        visited = set()

        def dfs(course: int) -> bool:
            if course in visited:
                return False

            if len(mapping[course]) == 0:
                return True

            visited.add(course)

            for pre in mapping[course]:
                if not dfs(pre):
                    return False
            
            visited.remove(course)
            mapping[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True
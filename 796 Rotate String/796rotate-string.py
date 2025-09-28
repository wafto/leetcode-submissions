class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        doubled = s + s

        for i in range(len(doubled) - len(goal)):
            if doubled[i: i + len(goal)] == goal:
                return True

        return False


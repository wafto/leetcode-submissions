class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        first, second = abs(z - x), abs(z - y)

        if first == second:
            return 0

        return 1 if first < second else 2
        
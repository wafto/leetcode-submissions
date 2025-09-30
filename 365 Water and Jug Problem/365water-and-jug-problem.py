class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False

        if x + y == target:
            return True

        if x == target or y == target:
            return True
        
        queue = deque([(0, 0)])
        seen = set([(0, 0)])

        while queue:
            a, b = queue.popleft()

            if a == target or b == target or a + b == target:
                return True

            states = [
                (x, b),
                (a, y),
                (0, b),
                (a, 0),
                (a + b - y, y) if a + b > y else (0, a + b),
                (x, a + b - x) if a + b > x else (a + b, 0)
            ]

            for state in states:
                if state not in seen:
                    seen.add(state)
                    queue.append(state)

        return False

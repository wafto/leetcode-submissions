class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        v, h = 0, 0
        distance = 0

        for i, c in enumerate(s):
            if c == 'N':
                v += 1
            elif c == 'S':
                v -= 1
            elif c == 'E':
                h += 1
            elif c == 'W':
                h -= 1

            distance = max(distance, min(abs(v) + abs(h) + k * 2, i + 1))
        
        return distance
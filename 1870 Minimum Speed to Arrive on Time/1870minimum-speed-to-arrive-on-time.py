class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour):
            return -1

        left, right = 1, 10 ** 7

        def at_speed(k: int) -> bool:
            total = 0
            for d in dist:
                total = ceil(total)
                total += d / k
            return total <= hour

        while left <= right:
            mid = (right + left) // 2

            if at_speed(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left



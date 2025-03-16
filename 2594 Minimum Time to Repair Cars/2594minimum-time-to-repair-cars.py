class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def repairable(min: int) -> bool:
            count = 0
            for r in ranks:
                count += int(math.sqrt(min / r))
                if count >= cars:
                    return True
            return count >= cars

        left, right = 1, ranks[0] * (cars ** 2)

        while left <= right:
            mid = (right + left) // 2

            if repairable(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
            
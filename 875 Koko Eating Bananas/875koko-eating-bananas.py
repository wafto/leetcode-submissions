class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def eatable_bananas(k: int) -> bool:
            total = 0
            for pile in piles:
                total += ceil(pile / k)
            return total <= h

        while left <= right:
            mid = (right + left) // 2

            if eatable_bananas(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

        
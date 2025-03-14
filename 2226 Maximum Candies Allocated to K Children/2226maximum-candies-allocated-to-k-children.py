class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)

        if total < k:
            return 0

        def piles_of(size: int) -> bool:
            count = 0
            for pile in candies:
                count += pile // size
                if count >= k:
                    return True
            return count >= k

        left, right = 1, total // k

        while left <= right:
            mid = (right + left) // 2

            if piles_of(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
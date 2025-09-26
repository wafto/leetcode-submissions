class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, (num // 2) + 1

        while left <= right:
            mid = (right + left) // 2
            square = mid ** 2

            if square < num:
                left = mid + 1
            else:
                right = mid - 1

        return (left ** 2) == num


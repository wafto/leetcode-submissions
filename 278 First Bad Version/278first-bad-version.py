# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        middle = n

        while left <= right:
            middle = left + (right - left) // 2

            if left == right:
                return right

            if not isBadVersion(middle):
                left = middle + 1
            else:
                right = middle

        return middle



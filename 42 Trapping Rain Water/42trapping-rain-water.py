class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left = [0] * n # max left
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i - 1])

        right = [0] * n # max right
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i + 1])

        ans = 0
        for i in range(n):
            minimum = min(left[i], right[i])
            ans += max(0, minimum - height[i])

        return ans

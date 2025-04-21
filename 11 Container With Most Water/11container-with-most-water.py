class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximal, n = 0, len(height)
        left, right = 0, n - 1

        while left < right:
            area = (right - left) * min(height[left], height[right])
            maximal = max(maximal, area)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maximal

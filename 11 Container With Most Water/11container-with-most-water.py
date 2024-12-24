class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxStore, currStore = 0, 0
        left, right = 0, len(height) - 1

        while left < right:
            currStore = min(height[left], height[right]) * (right - left)
            maxStore = max(maxStore, currStore)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxStore

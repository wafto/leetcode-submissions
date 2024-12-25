class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[0], height[len(height) - 1]
        output = 0

        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                output += maxLeft - height[left]
            else:
                right -= 1
                maxRight = max(maxRight, height[right])
                output += maxRight - height[right]

        return output
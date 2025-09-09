class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n, stack = len(heights), []
        ans = [0] * n

        for i in range(n - 1, -1, -1):
            height = heights[i]

            while stack and stack[-1] < height:
                stack.pop()
                ans[i] += 1

            if stack:
                ans[i] += 1
            
            stack.append(height)

        return ans
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ordered = sorted(heights.copy())
        ans = 0

        for i in range(len(heights)):
            if heights[i] != ordered[i]:
                ans += 1

        return ans

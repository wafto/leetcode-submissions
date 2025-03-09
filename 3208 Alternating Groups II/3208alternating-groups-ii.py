class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        left, ans = 0, 0

        for right in range(1, n + k - 1):
            if colors[(right - 1) % n] == colors[right % n]:
                left = right

            while right - left + 1 > k:
                left += 1

            if right - left + 1 == k:
                ans += 1

        return ans
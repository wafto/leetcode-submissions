class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        costs = [0] * n

        for i in range(n):
            costs[i] = abs(ord(s[i]) - ord(t[i]))

        
        left, curr = 0, 0
        ans = 0

        for right in range(n):
            curr += costs[right]

            while curr > maxCost:
                curr -= costs[left]
                left += 1

            ans = max(ans, right - left + 1)

        return ans

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse = True)
        s.sort(reverse = True)
        n, m, j = len(g), len(s), 0

        for i in range(n):
            greed = g[i]
            if j < m and greed <= s[j]:
                j += 1

        return j 

class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)

        if n < 3:
            return s
        
        ans = [s[0], s[1]]

        for i in range(2, n):
            if s[i] != s[i - 2] or s[i] != s[i - 1]:
                ans.append(s[i])
        
        return ''.join(ans)

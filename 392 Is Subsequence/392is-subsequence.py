class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, n = 0, len(s)

        for j in range(len(t)):
            if i < n and t[j] == s[i]:
                i += 1

        return i == n
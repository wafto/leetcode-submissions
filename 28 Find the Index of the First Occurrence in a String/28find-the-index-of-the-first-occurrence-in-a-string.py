class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)

        if n < m:
            return -1

        for i in range(n - m + 1):
            found = True
            for j in range(m):
                if needle[j] != haystack[i + j]:
                    found = False
                    break
            if found:
                return i

        return -1
            
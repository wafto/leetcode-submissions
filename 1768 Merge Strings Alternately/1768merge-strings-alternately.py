class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)
        ans = []

        for i in range(min(n, m)):
            ans.append(word1[i])
            ans.append(word2[i])

        word1 = word1 if n > m else word2

        for i in range(min(n, m), max(n, m)):
            ans.append(word1[i])

        return ''.join(ans)
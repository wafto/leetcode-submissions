class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        ans, i, nl = [], 0, min(n1, n2)

        while i < nl:
            ans.append(word1[i])
            ans.append(word2[i])
            i += 1

        j = i
        while j < n1:
            ans.append(word1[j])
            j += 1

        j = i
        while j < n2:
            ans.append(word2[j])
            j += 1

        return ''.join(ans)

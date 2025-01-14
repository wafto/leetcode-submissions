class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s1, s2 = len(word1), len(word2)
        i, j = 0, 0
        output = ''

        while i < s1 and j < s2:
            output += word1[i] + word2[j]
            i += 1
            j += 1

        while i < s1:
            output += word1[i]
            i += 1
        
        while j < s2:
            output += word2[j]
            j += 1

        return output




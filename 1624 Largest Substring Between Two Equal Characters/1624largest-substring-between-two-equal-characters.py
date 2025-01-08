class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        maxlength = -1

        for i in range(len(s)):
            j = s.rindex(s[i])
            maxlength = max(maxlength, j - 1 - i)

        return maxlength

        


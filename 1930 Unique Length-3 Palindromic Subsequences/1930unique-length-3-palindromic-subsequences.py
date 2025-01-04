class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        output = 0

        for letter in letters:
            i, j = s.index(letter), s.rindex(letter)
            between = set()

            for k in range(i + 1, j):
                between.add(s[k])
            
            output += len(between)

        return output
        

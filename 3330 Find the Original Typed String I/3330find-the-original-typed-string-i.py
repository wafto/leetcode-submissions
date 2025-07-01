class Solution:
    def possibleStringCount(self, word: str) -> int:
        dups = 0

        for i in range(1, len(word)):
            if word[i - 1] == word[i]:
                dups += 1

        return dups + 1
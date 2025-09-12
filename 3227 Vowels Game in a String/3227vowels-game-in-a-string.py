class Solution:
    def doesAliceWin(self, s: str) -> bool:
        count = 0

        for c in s:
            if c in 'aeiou':
                count += 1

        return count != 0
        
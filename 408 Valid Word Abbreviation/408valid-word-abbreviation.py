class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        m, n = len(word), len(abbr)

        while i < m and j < n:
            if abbr[j].isalpha():
                if abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[j] == '0':
                    return False
                count = 0
                while j < n and abbr[j].isdigit():
                    count = count * 10 + int(abbr[j])
                    j += 1
                i += count
        
        return i == m and j == n

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if word1 == word2:
            return True

        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        c1 = [0] * 26
        c2 = [0] * 26

        for i in range(len(word1)):
            c1[ord(word1[i]) - 97] += 1
            c2[ord(word2[i]) - 97] += 1

        if c1 == c2:
            return True

        c1.sort()
        c2.sort()

        return c1 == c2
        
            

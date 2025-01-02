class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = { chr(n): 0 for n in range(97, 123) }
        
        for c in magazine:
            letters[c] += 1

        for c in ransomNote:
            if letters[c] == 0:
                return False
            letters[c] -= 1

        return True
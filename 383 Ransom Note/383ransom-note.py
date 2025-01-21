class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h = [0] * 26
        
        for c in magazine:
            h[ord(c) - 97] += 1

        for c in ransomNote:
            if h[ord(c) - 97] == 0:
                return False
            h[ord(c) - 97] -= 1

        return True
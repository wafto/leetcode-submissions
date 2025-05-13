class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26
        ord_a = ord('a')

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            freq[ord_a - ord(s[i])] += 1
            freq[ord_a - ord(t[i])] -= 1

        return freq == ([0] * 26)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)
        ord_a = ord('a')
        
        if ns != nt:
            return False
        
        freq_s, freq_t = [0] * 26, [0] * 26
        
        for i in range(ns):
            freq_s[ord(s[i]) - ord_a] += 1
            freq_t[ord(t[i]) - ord_a] += 1

        return freq_s == freq_t
    
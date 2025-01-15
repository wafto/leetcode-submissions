class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s1, s2 = len(s), len(p)
        f = [0] * 26
        output = []

        for c in p:
            f[ord(c) - 97] += 1

        t = [0] * 26

        for c in s[:s2]:
            t[ord(c) - 97] += 1
        
        for i in range(s1 - s2 + 1):
            if i > 0:
                t[ord(s[i - 1]) - 97] -= 1
                t[ord(s[i + s2 - 1]) - 97] += 1
            anagram = True
            for k in range(26):
                if f[k] != t[k]:
                    anagram = False
                    break
            if anagram: 
                output.append(i)

        return output
            

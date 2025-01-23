class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest = ''

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i: j]
                if len(sub) > len(longest):
                    uniques = set(sub)
                    nice = True
                    for c in uniques:
                        if c.swapcase() not in uniques:
                            nice = False
                            break
                    if nice:
                        longest = sub

        return longest
                


        
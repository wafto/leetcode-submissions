class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        longest = ""

        if size == 1 or s == s[::-1]:
            return s

        for i in range(size):
            j = size - 1
            while j > 0:
                sub = s[i: j + i]
                if len(sub) > len(longest) and sub == sub[::-1]:
                    longest = sub
                j -= 1
        
        return longest
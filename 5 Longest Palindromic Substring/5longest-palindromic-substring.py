class Solution:
    def longestPalindrome(self, s: str) -> str:
        n, longest = len(s), s[0]

        def palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        if n == 1:
            return longest

        if n == 2:
            return s if palindrome(0, 1) else longest

        for i in range(n):
            for j in range(i, n):
                if j - i + 1 > len(longest) and palindrome(i, j):
                    longest = s[i: j + 1]

        return longest
        
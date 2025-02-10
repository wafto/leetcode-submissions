class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, chars = 0, set()
        longest = 0

        for right, char in enumerate(s):
            while char in chars:
                chars.remove(s[left])
                left += 1
            chars.add(char)
            longest = max(longest, right - left + 1)

        return longest
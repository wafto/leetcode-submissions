class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, longest = 0, 0
        chars = set()

        for right, char in enumerate(s):
            while char in chars:
                chars.remove(s[left])
                left += 1
            chars.add(char)
            longest = max(longest, right - left + 1)

        return longest

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n, longest, left = len(s), 0, 0
        existing = set()

        for right in range(n):
            while s[right] in existing:
                existing.remove(s[left])
                left += 1

            existing.add(s[right])
            longest = max(longest, len(existing))

        return longest
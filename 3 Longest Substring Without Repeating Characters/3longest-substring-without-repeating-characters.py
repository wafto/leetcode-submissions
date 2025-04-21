class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        longest, left = 0, 0

        for right, char in enumerate(s):
            while char in hashset:
                hashset.remove(s[left])
                left += 1
            
            hashset.add(char)
            longest = max(longest, len(hashset))

        return longest


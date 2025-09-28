class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        hashmap = {}
        left, longest = 0, 0

        for right in range(len(s)):
            if s[right] not in hashmap:
                hashmap[s[right]] = 0
            hashmap[s[right]] += 1

            while len(hashmap) > 2:
                hashmap[s[left]] -= 1

                if hashmap[s[left]] == 0:
                    del hashmap[s[left]]

                left += 1
    
            longest = max(longest, right - left + 1)

        return longest

                

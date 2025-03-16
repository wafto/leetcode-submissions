class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter, odd = Counter(s), 0

        for num in counter.values():
            if num & 1:
                odd += 1
            
        return odd <= 1
class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                break
            
            c = s[left]

            while left < len(s) and s[left] == c:
                left += 1

            while right >= 0 and s[right] == c:
                right -= 1
        
        return max(right - left + 1, 0)

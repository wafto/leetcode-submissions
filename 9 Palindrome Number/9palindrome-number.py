class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digits = str(x)
        left, right = 0, len(digits) - 1

        while left < right:
            if digits[left] != digits[right]:
                return False
            left, right = left + 1, right - 1

        return True        


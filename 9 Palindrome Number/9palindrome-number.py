class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True

        if x < 0 or x % 10 == 0:
            return False
        
        chain = str(x)
        left = 0
        right = len(chain) - 1

        while left < right:
            if chain[left] != chain[right]:
                return False
            left += 1
            right -= 1

        return True

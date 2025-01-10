class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()

        while left < right:
            cl, cr = ord(s[left]), ord(s[right])

            if not (cl >= 97 and cl <= 122) and not (cl >= 48 and cl <= 57):
                left += 1
                continue

            if not (cr >= 97 and cr <= 122) and not (cr >= 48 and cr <= 57):
                right -= 1
                continue

            if cr != cl:
                return False
            
            left += 1
            right -= 1
        
        return True

        
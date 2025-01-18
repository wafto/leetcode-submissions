class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = list(s)
        left, right = 0, len(letters) - 1

        while left < right:
            cl, cr = ord(letters[left]), ord(letters[right])
            
            if not ((cl >= 97 and cl <= 122) or (cl >= 65 and cl <= 90)):
                left += 1
                continue

            if not ((cr >= 97 and cr <= 122) or (cr >= 65 and cr <= 90)):
                right -= 1
                continue

            letters[left], letters[right] = letters[right], letters[left]
            left += 1
            right -= 1

        return ''.join(letters)

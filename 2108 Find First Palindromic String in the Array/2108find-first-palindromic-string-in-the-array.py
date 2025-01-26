class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        '''
        def palindrome(s: str) -> bool:
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        '''

        for word in words:
            if word == word[::-1]:
                return word
        
        return ''

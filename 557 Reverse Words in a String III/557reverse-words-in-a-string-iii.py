class Solution:
    def reverseWords(self, s: str) -> str:
        phrase = list(s)
        n = len(phrase)

        def reverse(left: int, right: int) -> None:
            while left < right:
                phrase[left], phrase[right] = phrase[right], phrase[left]
                left, right = left + 1, right - 1

        left = 0
        for right in range(n):
            if phrase[right] == ' ' and left < n:
                reverse(left, right - 1)
                left = right + 1

        if left < right:
            reverse(left, right)

        return ''.join(phrase)


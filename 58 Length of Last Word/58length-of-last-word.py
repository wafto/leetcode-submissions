class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        total = len(s)

        end = total - 1

        while end >= 0:
            if s[end] == ' ':
                end -= 1
            else:
                break

        start = end

        while start >= 0:
            if s[start] == ' ':
                break
            else:
                start -= 1

        return end - start
        
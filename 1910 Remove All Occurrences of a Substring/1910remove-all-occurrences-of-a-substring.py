class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part = list(part)
        m = len(part)

        for char in s:
            stack.append(char)
            n = len(stack)

            if n >= m and stack[-m:] == part:
                del stack[-m:]

        return ''.join(stack)

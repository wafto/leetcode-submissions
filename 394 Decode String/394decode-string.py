class Solution:
    def decodeString(self, s: str) -> str:
        num, acc = 0, ''
        stack = []

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                stack.append((acc, num))
                num = 0
                acc = '' 
            elif c == ']':
                w, n = stack.pop()
                acc = w + n * acc
            else:
                acc += c

        return acc
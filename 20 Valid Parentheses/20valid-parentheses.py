class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for c in s:
            if c in mapping:
                stack.append(c)
            elif not stack:
                return False
            elif mapping[stack[-1]] != c:
                return False
            else:
                stack.pop()

        return len(stack) == 0
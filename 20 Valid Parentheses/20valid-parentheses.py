class Solution:
    def isValid(self, s: str) -> bool:
        size = len(s)
        stack = []

        if size & 1 == 1:
            return False

        for bracket in s:
            if bracket in ['(', '[', '{']:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                last = stack[-1]
                if last == '(' and bracket == ')':
                    stack.pop()
                elif last == '[' and bracket == ']':
                    stack.pop()
                elif last == '{' and bracket == '}':
                    stack.pop()
                else:
                    return False

        return not stack

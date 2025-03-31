class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        brackets = {'(': ')', '{': '}', '[': ']'}
        stack = []

        if n & 1:
            return False

        for c in s:
            if c in brackets:
                stack.append(c)
            elif stack:
                last = stack.pop()
                if last not in brackets:
                    return False
                if brackets[last] != c:
                    return False
            else:
                return False
        
        return not stack



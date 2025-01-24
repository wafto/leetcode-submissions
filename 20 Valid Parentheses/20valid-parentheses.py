class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(': ')', '[': ']', '{': '}'}
        stack = []

        for bracket in s:
            if bracket in mapping:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if mapping[last] != bracket:
                    return False
        
        return not stack




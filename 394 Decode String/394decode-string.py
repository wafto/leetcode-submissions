class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != ']':
                stack.append(c)
            else:
                sub = ''
                while stack[-1] != '[':
                    sub = stack.pop() + sub
                
                stack.pop()
                
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                
                stack.append(int(num) * sub)
        
        return ''.join(stack)
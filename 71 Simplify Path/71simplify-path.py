class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        acc = ''

        for c in path:
            if c == '/':
                if acc == '..':
                    if stack: stack.pop()
                elif acc and acc != '.':
                    stack.append(acc)
                else:
                    pass
                acc = ''
            else:   
                acc += c

        if acc:
            if acc == '..':
                if stack: stack.pop()
            else:
                if acc != '.': stack.append(acc)

        return '/' + '/'.join(stack)

            

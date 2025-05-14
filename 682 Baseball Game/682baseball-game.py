class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op.isnumeric() or op[0] == '-':
                stack.append(int(op))
            elif op == '+' and len(stack) >= 2:
                stack.append(stack[-1] + stack[-2])
            elif op == 'D' and stack:
                stack.append(stack[-1] * 2)
            elif op == 'C' and stack:
                stack.pop()

        return sum(stack)

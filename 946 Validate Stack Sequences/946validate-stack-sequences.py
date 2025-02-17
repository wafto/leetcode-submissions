class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack, i, n = [], 0, len(popped)

        for num in pushed:
            stack.append(num)

            while stack and i < n and stack[-1] == popped[i]:
                stack.pop()
                i += 1
            
        return not stack
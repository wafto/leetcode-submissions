class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        a, answer = 0, deque()

        while i >= 0 or j >= 0:
            n1 = 0 if i < 0 else int(num1[i]) 
            n2 = 0 if j < 0 else int(num2[j])
            sumnum = n1 + n2 + a
            answer.appendleft(str(sumnum % 10))
            a = 1 if sumnum > 9 else 0
            i, j = i - 1, j - 1

        if a:
            answer.appendleft('1')

        return ''.join(answer)

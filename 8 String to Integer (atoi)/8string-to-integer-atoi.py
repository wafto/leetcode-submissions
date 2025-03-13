class Solution:
    def myAtoi(self, s: str) -> int:
        n, neg = len(s), False
        digits = deque()

        i = 0
        while i < n and s[i] == ' ':
            i += 1

        if i < n and s[i] in ['-', '+']:
            neg = s[i] == '-'
            i += 1

        while i < n and s[i] == '0':
            i += 1

        while i < n and s[i].isnumeric():
            digits.appendleft(int(s[i]))
            i += 1

        ans = 0
        for i in range(len(digits)):
            ans += digits[i] * (10 ** i)

        if neg:
            return max(-ans, -2 ** 31)
        
        return min(ans, (2 ** 31) - 1)

        

        

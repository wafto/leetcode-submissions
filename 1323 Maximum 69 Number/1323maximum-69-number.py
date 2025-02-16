class Solution:
    def maximum69Number(self, num: int) -> int:
        digits = deque()

        while num:
            digits.appendleft(num % 10)
            num //= 10

        for i in range(len(digits)):
            if digits[i] == 6:
                digits[i] = 9
                break

        i, ans = 0, 0
        while digits:
            ans += digits.pop() * (10 ** i)
            i += 1
        
        return ans
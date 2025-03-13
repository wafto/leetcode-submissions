class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n, acc = len(digits), 1
        ans = deque()

        for i in range(n - 1, -1, -1):
            addition = digits[i] + acc
            ans.appendleft(addition % 10)
            acc = 1 if addition == 10 else 0

        if acc:
            ans.appendleft(1)

        return list(ans)

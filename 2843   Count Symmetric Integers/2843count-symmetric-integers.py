class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for num in range(low, high + 1):
            s = str(num)
            n = len(s)

            if n & 1:
                continue

            m = n // 2

            if sum(int(d) for d in s[:m]) == sum(int(d) for d in s[m:]):
                count += 1

        return count
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        n1, n2 = 1, n - 1

        def has_zero(num: int) -> bool:
            return '0' in str(num)

        while has_zero(n1) or has_zero(n2):
            n1 += 1
            n2 = n - n1

        return [n1, n2]

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        lut = [n + 27 for n in range(26)]

        for i, c, in enumerate(order):
            lut[ord(c) - 97] = i

        data = sorted(s, key=lambda c: lut[ord(c) - 97])

        return ''.join(data)
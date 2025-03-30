class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = [-1] * 26
        ord_a = ord('a')

        for i, c in enumerate(s):
            last_index[ord(c) - ord_a] = i

        size, end = 0, 0
        ans = []

        for i, c in enumerate(s):
            size += 1
            end = max(end, last_index[ord(c) - ord_a])

            if i == end:
                ans.append(size)
                size = 0

        return ans


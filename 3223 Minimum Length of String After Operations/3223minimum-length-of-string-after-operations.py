class Solution:
    def minimumLength(self, s: str) -> int:
        count = {}

        for c in s:
            count[c] = 1 + count.get(c, 0)

        removed = 0
        for n in count.values():
            if n & 1:
                removed += n - 1
            else:
                removed += n - 2
            
        return len(s) - removed
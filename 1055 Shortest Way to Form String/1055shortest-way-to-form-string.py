class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        existing = set(source)
        n = len(source)
        i, ans = 0, 0

        for char in target:
            if char not in existing:
                return -1

            if i == 0:
                ans += 1

            while source[i] != char:
                i = (i + 1) % n
                if i == 0:
                    ans += 1
            
            i = (i + 1) % n

        return ans


            

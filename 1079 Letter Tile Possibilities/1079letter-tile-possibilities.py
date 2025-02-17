class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def backtracking() -> int:
            ans = 0
            for key in count:
                if count[key] > 0:
                    count[key] -= 1
                    ans += 1 + backtracking()
                    count[key] += 1
            return ans

        return backtracking()

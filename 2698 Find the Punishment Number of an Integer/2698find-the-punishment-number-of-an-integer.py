class Solution:
    def punishmentNumber(self, n: int) -> int:
        ans = 0

        def backtracking(i: int, cur: int, target: int, string: str) -> bool:
            if i == len(string) and target == cur:
                return True

            for j in range(i, len(string)):
                s = string[i: j + 1]
                if backtracking(j + 1, cur + int(s), target, string):
                    return True
            
            return False
        
        for i in range(1, n + 1):
            if backtracking(0, 0, i, str(i * i)):
                ans += i * i

        return ans



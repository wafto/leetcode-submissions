class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (n * 2 - 1)
        seen = set()

        def backtrack(i: int) -> bool:
            if i == len(ans):
                return True
            
            for num in range(n, 0, -1):
                if num in seen:
                    continue
                
                if num > 1 and (i + num >= len(ans) or ans[i + num] != 0):
                    continue

                seen.add(num)
                ans[i] = num
                if num > 1:
                    ans[i + num] = num

                j = i + 1
                while j < len(ans) and ans[j] != 0:
                    j += 1

                if backtrack(j):
                    return True

                seen.remove(num)
                ans[i] = 0
                if num > 1:
                    ans[i + num] = 0

            return False

        backtrack(0)
        return ans

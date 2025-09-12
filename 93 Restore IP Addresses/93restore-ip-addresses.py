class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n, ans = len(s), []

        def backtracking(i: int, curr: List[str]) -> None:
            if len(curr) == 4 and i == n:
                ans.append('.'.join(curr))
                return

            if len(curr) == 4:
                return
            
            for j in range(i, min(i + 3, n)):
                sub = s[i: j + 1]

                if len(sub) > 1 and sub[0] == '0':
                    break

                if int(sub) > 255:
                    break

                curr.append(sub)
                backtracking(j + 1, curr)
                curr.pop()

        backtracking(0, [])
        return ans
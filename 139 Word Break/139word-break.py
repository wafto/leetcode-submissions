class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[-1] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                lower, upper = i, i + len(word)
                if upper <= n and s[lower: upper] == word:
                    dp[lower] = dp[upper]
                if dp[lower]:
                    break
        
        return dp[0]
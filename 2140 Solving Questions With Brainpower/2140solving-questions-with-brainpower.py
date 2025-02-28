class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            score, brainpower = questions[i]
            j = min(i + brainpower + 1, n)
            dp[i] = max(dp[i + 1], score + dp[j])

        return dp[0]
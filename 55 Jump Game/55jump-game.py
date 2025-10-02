class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return goal == 0
        """

        """
        @cache
        def dp(i: int) -> bool:
            if i >= len(nums) - 1:
                return True

            if nums[i] == 0:
                return False

            for j in range(i + 1, i + nums[i] + 1):
                if dp(j):
                    return True

            return False

        return dp(0)
        """

        n = len(nums)
        dp = [False] * n
        dp[-1] = True

        for i in range(n - 2, -1, -1):
            if i + nums[i] >= n:
                dp[i] = True
                continue
            
            for j in range(i + 1, i + nums[i] + 1):
                if dp[j]: 
                    dp[i] = True
                    break
                    
        return dp[0]

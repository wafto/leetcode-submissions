class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack, ans = [], []
        n = len(nums)

        for i, num in enumerate(nums):
            while stack and stack[-1] > num and n - i > k - len(stack):
                stack.pop()

            stack.append(num)

        return stack[:k]
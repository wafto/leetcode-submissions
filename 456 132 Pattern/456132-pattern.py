class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        cmin, stack = nums[0], []

        for i in range(1, len(nums)):
            num = nums[i]

            while stack and stack[-1][0] <= num:
                stack.pop()

            if stack and stack[-1][1] < num:
                return True 

            stack.append((num, cmin))
            cmin = min(cmin, num)

        return False
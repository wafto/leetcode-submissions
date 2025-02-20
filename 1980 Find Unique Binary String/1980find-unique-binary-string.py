class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums, bits = set(nums), len(nums[0])
        generable = 2 ** bits

        def tobin(num: int) -> str:
            ans = deque()
            while num:
                ans.appendleft('1' if num & 1 else '0')
                num >>= 1
            while len(ans) < bits:
                ans.appendleft('0')
            return ''.join(ans)

        for i in range(generable):
            option = tobin(i)
            if option not in nums:
                return option
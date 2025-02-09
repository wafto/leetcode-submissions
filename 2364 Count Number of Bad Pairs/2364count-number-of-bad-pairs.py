class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        good, n = 0, len(nums)
        counter = defaultdict(int)

        for i in range(n):
            good += counter[nums[i] - i]
            counter[nums[i] - i] += 1

        return ((n * (n - 1)) // 2) - good

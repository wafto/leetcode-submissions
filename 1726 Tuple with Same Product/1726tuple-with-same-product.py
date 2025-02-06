class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        prods = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prods[nums[i] * nums[j]] += 1

        ans = 0

        for x in prods.values():
            ans += ((x * (x - 1)) // 2) << 3

        return ans 
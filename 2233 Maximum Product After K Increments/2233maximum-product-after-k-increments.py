class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(k):
            top = heapq.heappop(nums)
            heapq.heappush(nums, top + 1)

        ans = 1
        for num in nums:
            ans *= num
            ans %= (10 ** 9) + 7

        return ans
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [[1000 - n, n] for n in nums]
        heap = heapq.heapify(nums)
        while k > 1:
            heapq.heappop(nums)
            k -= 1
        _, n = nums[0]
        return n
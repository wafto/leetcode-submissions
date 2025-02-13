class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        nums = [-num for num in nums]
        half = total / 2
        heapq.heapify(nums)
        
        curr, op = total, 0
        while curr > half:
            num = heapq.heappop(nums) / 2
            curr += num
            heapq.heappush(nums, num)
            op += 1

        return op
            
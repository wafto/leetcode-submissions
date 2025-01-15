class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        size = len(nums)

        if size == 1:
            return nums[0]

        acc = sum(nums[:k])
        avg = acc / k 

        for i in range(k, size):
            acc += nums[i] - nums[i - k]
            avg = max(avg, acc / k)

        return avg



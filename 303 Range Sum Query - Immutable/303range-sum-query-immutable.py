class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = []
        total = 0
        for n in nums:
            total += n
            self.nums.append(total)        

    def sumRange(self, left: int, right: int) -> int:
        presum = self.nums[left - 1] if left > 0 else 0
        return self.nums[right] - presum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
class Solution:

    def __init__(self, nums: List[int]):
        self.seed = nums
        
    def reset(self) -> List[int]:
        return self.seed

    def shuffle(self) -> List[int]:
        copy = self.seed.copy()
        index = len(copy) - 1
        while index > 0:
            rand = random.randint(0, index)
            copy[rand], copy[index] = copy[index], copy[rand]
            index -= 1
        return copy
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
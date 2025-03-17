class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for cnt in count.values():
            if cnt & 1:
                return False

        return True
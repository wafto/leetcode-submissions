class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = dict()

        for n in nums:
            frequency[n] = 1 + frequency.get(n, 0)

        return sorted(nums, key=lambda n: (frequency[n], -n))

       

        
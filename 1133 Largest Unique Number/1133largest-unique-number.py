class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        for num in nums:
            hashmap[num] += 1

        largest = -1
        
        for num, count in hashmap.items():
            if count == 1:
                largest = max(largest, num)

        return largest
        
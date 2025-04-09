class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ops, greater = 0 , set()

        for num in nums:
            if num < k:
                return -1
            elif num > k and num not in greater:
                ops += 1
                greater.add(num)
            
        return ops




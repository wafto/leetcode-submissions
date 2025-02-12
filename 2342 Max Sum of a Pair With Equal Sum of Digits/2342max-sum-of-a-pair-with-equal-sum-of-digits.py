class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mapping = dict()
        maximum = -1

        def digit_sum(n: int) -> int:
            ans = 0
            while n > 0:
                ans += n % 10
                n //= 10
            return ans

        for num in nums:
            dsum = digit_sum(num)
            
            if dsum in mapping:
                maximum = max(maximum, mapping[dsum] + num)
                mapping[dsum] = max(mapping[dsum], num)
            else:
                mapping[dsum] = num

        return maximum
            

class Solution:

    def maximumSum(self, nums: List[int]) -> int:
        hashmap = {}
        ans = -1

        def digitsum(num: int) -> int:
            total = 0
            while num:
                total += num % 10
                num //= 10
            return total

        for num in nums:
            sd = digitsum(num)

            if sd not in hashmap:
                hashmap[sd] = num
            else:
                hashv = hashmap[sd]
                ans = max(ans, hashv + num)
                hashmap[sd] = max(hashv, num)

        return ans
            
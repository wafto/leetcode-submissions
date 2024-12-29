class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        output = 0
        currSum = 0
        hm = {0: 1}

        for n in nums:
            currSum += n
            diff = currSum - k

            if diff in hm:
                output += hm[diff]

            hm[currSum] = 1 + hm.get(currSum, 0)

        return output

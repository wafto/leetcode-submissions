class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashmap = defaultdict(int)
        count = 0

        for num in time:
            if num % 60 == 0:
                count += hashmap[0]
            else:
                count += hashmap[60 - num % 60]
            hashmap[num % 60] += 1

        return count
        
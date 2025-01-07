class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        table = dict()
        
        for n in nums:
            table[n] = 1 + table.get(n, 0)

        output = 0
        
        for c in table.values():
            output += (c - 1) * c // 2
            
        return output
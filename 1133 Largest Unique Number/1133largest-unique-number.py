class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        
        for n in nums:
            counter[n] += 1
            
        largest = -1 
        
        for n, c in counter.items():
            if c == 1:
                largest = max(largest, n)
            
        return largest
            
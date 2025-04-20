class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        total = 0
        
        for x in count:
            total += ceil(float(count[x]) / (x + 1)) * (x + 1)
        
        return int(total)
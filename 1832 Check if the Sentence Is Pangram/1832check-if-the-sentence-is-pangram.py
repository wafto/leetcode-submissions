class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        
        for c in sentence:
            seen.add(c)
            
        return len(seen) == 26
            
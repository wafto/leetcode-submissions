class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        i = 0
        
        for direction, amount in shift:
            i += amount if direction == 1 else -amount

        l = len(s)

        if l == 0:
            return s

        i = i % l 
        
        if i < 0:
            return s[i * -1:] + s[: i * -1]
        else:
            return s[l - i:] + s[: l - i]

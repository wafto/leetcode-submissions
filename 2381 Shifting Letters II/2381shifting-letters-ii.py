class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        size = len(s)
        ps = [0] * (size + 1)

        for start, end, direction in shifts:
            offset = 1 if direction == 1 else -1
            ps[start] += offset
            ps[end + 1] -= offset

        for i in range(1, size):
            ps[i] += ps[i - 1]

        output = ''
        
        for i in range(size):
            c = (ord(s[i]) - 97 + ps[i]) % 26
            output += chr(c + 97)

        return output

            

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        positions = dict()
        counterR = [0] * rows
        counterC = [0] * cols

        for r in range(rows):
            for c in range(cols):
                positions[mat[r][c]] = (r, c)
                
        for i, num in enumerate(arr):
            r, c = positions[num]
            
            counterR[r] += 1
            counterC[c] += 1

            if counterR[r] == cols or counterC[c] == rows:
                return i
            
        return -1

        
                    


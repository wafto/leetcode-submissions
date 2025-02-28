class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)

        prev = [str2[j:] for j in range(m)]
        prev.append('')

        for i in range(n -1, -1, -1):
            curr = [''] * m
            curr.append(str1[i:])
            
            for j in range(m - 1, -1, -1):
                if str1[i] == str2[j]:
                    curr[j] = str1[i] + prev[j + 1]
                else:
                    s1 = str1[i] + prev[j]
                    s2 = str2[j] + curr[j + 1]
                    curr[j] = s1 if len(s1) < len(s2) else s2
                    
            prev = curr

        return curr[0]
    

        memo = {}
        
        def backtrack(i: int, j: int) -> str:
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(str1):
                return str2[j:]
            
            if j == len(str2):
                return str1[i:]
            
            if str1[i] == str2[j]:
                return str1[i] + backtrack(i + 1, j + 1)
            
            seq1 = str1[i] + backtrack(i + 1, j)
            seq2 = str2[j] + backtrack(i, j + 1)

            memo[(i, j)] = seq1 if len(seq1) <= len(seq2) else seq2

            return memo[(i, j)]

        return backtrack(0, 0)
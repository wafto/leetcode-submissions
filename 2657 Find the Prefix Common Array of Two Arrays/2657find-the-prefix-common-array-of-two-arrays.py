class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        existing = set()
        C = [0] * len(A)
        count = 0

        for i in range(len(A)):
            if A[i] not in existing:
                existing.add(A[i])
            else:
                count += 1
            
            if B[i] not in existing:
                existing.add(B[i])
            else:
                count += 1

            C[i] = count

        return C

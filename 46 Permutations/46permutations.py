class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for num in nums:
            aux = []
            for perm in permutations:
                for i in range(len(perm) + 1):
                    copy = perm.copy()
                    copy.insert(i, num)
                    aux.append(copy)
            permutations = aux

        return permutations

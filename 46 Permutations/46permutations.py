class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = [[]]

        for num in nums:
            npermutations = []
            for perm in permutations:
                for i in range(len(perm) + 1):
                    cp = perm.copy()
                    cp.insert(i, num)
                    npermutations.append(cp)
            permutations = npermutations

        return permutations
            
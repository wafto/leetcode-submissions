class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = []
        counter = Counter(nums)

        def backtracking(curr: List[int]) -> None:
            if len(curr) == len(nums):
                perms.append(curr.copy())
                return

            for num, count in counter.items():
                if count < 1:
                    continue
                
                counter[num] -= 1
                curr.append(num)
                backtracking(curr)
                curr.pop()
                counter[num] += 1

        backtracking([])
        return perms
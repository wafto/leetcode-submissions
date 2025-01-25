class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = [deque()]
        mapping = {}

        for i, num in enumerate(sorted(nums)):
            if groups[-1] and num - groups[-1][-1] > limit:
                groups.append(deque())
            groups[-1].append(num)
            mapping[num] = len(groups) - 1

        ans = []
        for num in nums:
            ans.append(groups[mapping[num]].popleft())

        return ans



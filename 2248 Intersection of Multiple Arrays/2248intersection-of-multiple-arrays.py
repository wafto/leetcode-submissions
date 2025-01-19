class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        hm = defaultdict(int)
        rows = len(nums)

        for row in nums:
            for n in row:
                hm[n] += 1

        ans = []
        
        for n, c in hm.items():
            if c == rows:
                ans.append(n)

        ans.sort()

        return ans
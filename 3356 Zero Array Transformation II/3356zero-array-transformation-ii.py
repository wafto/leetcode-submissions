class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n, q = len(nums), len(queries)
        diff = [0] * (n + 1)
        pos, curr = 0, 0

        for i in range(n):
            while curr + diff[i] < nums[i]:
                if pos == q:
                    return -1
                
                start, end, val = queries[pos]
                pos += 1

                if end < i:
                    continue

                diff[max(i, start)] += val
                diff[end + 1] -= val

                curr += diff[i]
            
        return pos




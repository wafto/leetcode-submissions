class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapping = {}

        for n in nums:
            mapping[n] = 1 + mapping.get(n, 0)

        bucket = [[] for _ in range(len(nums) + 1)]
        for key, val in mapping.items():
            bucket[val].append(key)
        
        output = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                output.extend(bucket[i])
            if len(output) >= k:
                break

        return output[0:k]
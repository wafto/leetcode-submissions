class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        data = [(-v, x) for x, v in count.items()]
        heapify(data)
        ans = []

        for _ in range(k):
            ans.append(heappop(data)[1])

        return ans

        
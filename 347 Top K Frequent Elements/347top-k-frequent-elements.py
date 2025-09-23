class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        heap = [(-cnt, num) for num, cnt in count.items()]
        heapify(heap)

        ans = []
        
        for _ in range(k):
            ans.append(heappop(heap)[1])

        return ans

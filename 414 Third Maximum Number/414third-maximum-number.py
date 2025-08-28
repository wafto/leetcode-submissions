class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        minheap = []
        seen = set()

        for num in nums:
            if num in seen:
                continue

            seen.add(num)

            if len(minheap) < 3:
                heappush(minheap, num)
            elif minheap[0] < num:
                heappush(minheap, num)
                heappop(minheap)

        return minheap[0] if len(minheap) >= 3 else minheap[-1]

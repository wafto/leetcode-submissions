class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        cost = 0

        while len(sticks) > 1:
            stick = heappop(sticks) + heappop(sticks)
            heappush(sticks, stick)
            cost += stick

        return cost


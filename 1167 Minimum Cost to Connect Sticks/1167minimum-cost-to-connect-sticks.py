class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cost = 0

        while len(sticks) > 1:
            stick = heapq.heappop(sticks) + heapq.heappop(sticks)
            cost += stick
            heapq.heappush(sticks, stick)

        return cost

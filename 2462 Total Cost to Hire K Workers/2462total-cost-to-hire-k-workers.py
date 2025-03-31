class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        answer = 0

        for i in range(candidates):
            heap.append((costs[i], 0))

        for i in range(max(candidates, len(costs) - candidates), len(costs)):
            heap.append((costs[i], 1))

        heapq.heapify(heap)
        head, tail = candidates, len(costs) - 1 - candidates

        for _ in range(k):
            cost, section = heapq.heappop(heap)
            answer += cost
            if head <= tail: 
                if section == 0:
                    heappush(heap, (costs[head], 0))
                    head += 1
                else:
                    heappush(heap, (costs[tail], 1))
                    tail -= 1

        return answer



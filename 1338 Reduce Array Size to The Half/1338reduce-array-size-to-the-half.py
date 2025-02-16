class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n, heap = len(arr), [-v for v in Counter(arr).values()]
        heapq.heapify(heap)
        target, count = n // 2, 0

        while heap and target > 0:
            target += heapq.heappop(heap)
            count += 1

        return count
        

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapify(heap)

        for _ in range(1, k):
            heappop(heap)

        return -heap[0]


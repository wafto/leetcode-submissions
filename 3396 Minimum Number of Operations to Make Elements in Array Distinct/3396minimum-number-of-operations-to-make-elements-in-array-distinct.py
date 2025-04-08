class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        queue = deque(nums)
        operations = 0

        while queue:
            if all(v <= 1 for v in count.values()):
                break

            operations += 1

            for _ in range(min(3, len(queue))):
                count[queue.popleft()] -= 1

        return operations
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        answer = []

        for i, n in enumerate(nums):
            while queue and n > nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)
            
            if queue[0] + k == i:
                queue.popleft()

            if i >= k - 1:
                answer.append(nums[queue[0]])

        return answer
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        queue = deque()

        for i, temp in enumerate(temperatures):
            while queue and temperatures[queue[-1]] < temp:
                j = queue.pop()
                answer[j] = i - j
            queue.append(i)

        return answer
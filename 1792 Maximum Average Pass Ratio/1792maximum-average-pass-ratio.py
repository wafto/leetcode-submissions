class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(passed: int, students: int) -> float:
            return ((passed + 1) / (students + 1)) - (passed / students)

        rates = [(-gain(p, s), p, s) for p, s in classes]
        heapify(rates)

        for _ in range(extraStudents):
            r, p, s = heappop(rates)
            p, s = p + 1, s + 1
            heappush(rates, (-gain(p, s), p, s))

        return sum(r[1] / r[2] for r in rates) / len(classes)
        
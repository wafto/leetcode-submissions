class RecentCounter:
    def __init__(self):
        self.reqs = deque()

    def ping(self, t: int) -> int:
        self.reqs.append(t)

        while self.reqs[0] < t - 3000:
            self.reqs.popleft()

        return len(self.reqs)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
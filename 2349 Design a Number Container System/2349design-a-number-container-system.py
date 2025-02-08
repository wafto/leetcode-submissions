class NumberContainers:

    def __init__(self):
        self.number_indices = defaultdict(list)
        self.index_number = {}

    def change(self, index: int, number: int) -> None:
        self.index_number[index] = number 
        heapq.heappush(self.number_indices[number], index)

    def find(self, number: int) -> int:
        if not self.number_indices[number]:
            return -1
        while self.number_indices[number]:
            index = self.number_indices[number][0]
            if self.index_number.get(index) == number:
                return index
            heapq.heappop(self.number_indices[number])
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
class TwoSum:

    def __init__(self):
        self.hashmap = defaultdict(int)

    def add(self, number: int) -> None:
        self.hashmap[number] += 1
        
    def find(self, value: int) -> bool:
        for num, count in self.hashmap.items():
            diff = value - num
            if num != diff and diff in self.hashmap:
                return True
            if num == diff and self.hashmap[num] > 1:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
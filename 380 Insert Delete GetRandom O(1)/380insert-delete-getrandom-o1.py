class RandomizedSet:

    def __init__(self):
       self.dict = {}
       self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        
        index = self.dict[val]
        del self.list[index]
        ndict = {}
        for k, i in self.dict.items():
            if i == index:
                continue
            ndict[k] = i if i < index else i - 1
        self.dict = ndict
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
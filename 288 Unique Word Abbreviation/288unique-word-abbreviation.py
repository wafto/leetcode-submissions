class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.map = defaultdict(set)
        
        for word in dictionary:
            self.map[self.shorten(word)].add(word)
        
    def isUnique(self, word: str) -> bool:
        short = self.shorten(word)
        
        if short not in self.map:
            return True
        
        return len(self.map[short]) == 1 and word in self.map[short]

    def shorten(self, w: str) -> str:
        return w if len(w) < 3 else f'{w[0]}{str(len(w) - 2)}{w[-1]}'
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
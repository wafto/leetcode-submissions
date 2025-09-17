class Food:
    def __init__(self, rating, name):
        self.name = name
        self.rating = rating

    def __lt__(self, other):
        if self.rating == other.rating:
            return self.name < other.name
        return self.rating > other.rating

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.mfoods = {}
        self.mcousines = {}
        self.cousines_foods = defaultdict(list)

        for i in range(len(foods)):
            self.mfoods[foods[i]] = ratings[i]
            self.mcousines[foods[i]] = cuisines[i]
            heappush(self.cousines_foods[cuisines[i]], Food(ratings[i], foods[i]))

    def changeRating(self, food: str, newRating: int) -> None:
        self.mfoods[food] = newRating
        name = self.mcousines[food]
        heappush(self.cousines_foods[name], Food(newRating, food))

    def highestRated(self, cuisine: str) -> str:
        highest = self.cousines_foods[cuisine][0]

        while self.mfoods[highest.name] != highest.rating:
            heappop(self.cousines_foods[cuisine])
            highest = self.cousines_foods[cuisine][0]

        return highest.name



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
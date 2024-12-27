class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        tuples = []
        
        for i in range(len(names)):
            tuples.append((heights[i], names[i]))

        tuples.sort(key=lambda t: t[0], reverse=True)

        return list(map(lambda t: t[1], tuples))
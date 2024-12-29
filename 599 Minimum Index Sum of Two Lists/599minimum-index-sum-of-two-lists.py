class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mp = { s: i for i, s in enumerate(list1) }
        words = []

        for index, word in enumerate(list2):
            if word in mp:
                isum = index + mp[word]
                words.append((isum, word))

        if not words:
            return []

        words.sort()
        lowest = words[0][0]

        i = 0
        output = []

        while i < len(words):
            if words[i][0] == lowest:
                output.append(words[i][1])
            else:
                break
            i += 1

        return output

        
        
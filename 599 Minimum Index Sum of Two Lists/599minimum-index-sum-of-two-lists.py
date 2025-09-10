class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashmap = {w: i for i, w in enumerate(list1)}
        intersected = []
        leastsum = float('inf')

        for i, word in enumerate(list2):
            if word in hashmap:
                intersected.append((word, i + hashmap[word]))
                leastsum = min(leastsum, i + hashmap[word])

        answer = []

        for word, score in intersected:
            if score == leastsum:
                answer.append(word)

        return answer

        

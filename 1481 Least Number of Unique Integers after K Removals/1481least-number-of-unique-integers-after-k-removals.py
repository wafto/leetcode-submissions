class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        data = sorted(counter.values(), reverse=True)

        while k:
            if data[-1] <= k:
                k -= data[-1]
                data.pop()
            else:
                break
            
        return len(data)
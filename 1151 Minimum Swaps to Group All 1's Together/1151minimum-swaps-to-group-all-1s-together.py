class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n, ones = len(data), 0
        left, curr = 0, 0
        minimal = n + 1

        for i in range(n):
            if data[i]:
                ones += 1
        
        for right in range(n):
            curr += data[right]

            if right - left + 1 < ones:
                continue

            while right - left + 1 > ones:
                curr -= data[left]
                left += 1

            minimal = min(minimal, ones - curr)

        return minimal

            

        



class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        output = 0
        curSum = sum(arr[:k - 1])

        for i in range(len(arr) - k + 1):
            curSum += arr[i + k - 1]
            if (curSum / k) >= threshold:
                output += 1
            curSum -= arr[i]

        return output
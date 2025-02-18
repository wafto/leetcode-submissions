class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = []

        prev = 0
        for num in nums:
            prev += num
            prefix.append(prev)

        def binary_search(target: int) -> int:
            left, right = 0, len(prefix) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if prefix[mid] == target:
                    return mid + 1
                elif prefix[mid] > target: 
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return len(prefix) if ans == -1 else ans

        return [binary_search(q) for q in queries]


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n, ans = len(nums), 1

        prime_scores = []
        for num in nums:
            score = 0
            for f in range(2, int(sqrt(num)) + 1):
                if num % f == 0:
                    score += 1
                    while num % f == 0:
                        num //= f
            if num >= 2:
                score += 1
            prime_scores.append(score)

        left_bound = [-1] * n
        right_bound = [n] * n

        stack = []

        for i, score in enumerate(prime_scores):
            while stack and prime_scores[stack[-1]] < score:
                j = stack.pop()
                right_bound[j] = i
            if stack:
                left_bound[i] = stack[-1]
            stack.append(i)
            
        heap = [(-num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        while heap and k > 0:
            num, i = heapq.heappop(heap)

            num = -num
            score = prime_scores[i]

            left_cnt = i - left_bound[i]
            right_cnt = right_bound[i] - i

            count = left_cnt * right_cnt
            operations = min(count, k)
            ans = (ans * pow(num, operations, MOD)) % MOD
            k -= operations

        return ans

class Solution:
    def isHappy(self, n: int) -> bool:
        
        def digits(num: int) -> List[int]:
            answer = []
            while num > 0:
                answer.append(num % 10)
                num //= 10
            return answer

        def squared_sum(num: int) -> int:
            return sum([d * d for d in digits(num)])

        seen = set()

        while True:
            n = squared_sum(n)
            if n == 1:
                return True
            elif n not in seen:
                seen.add(n)
            else:
                break

        return False

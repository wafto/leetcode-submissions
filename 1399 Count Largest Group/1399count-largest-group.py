class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = defaultdict(int)
        largest, count = 0, 0
        
        def sum_digits(num: int) -> int:
            total = 0
            while num > 0:
                total += num % 10
                num //= 10
            return total

        for num in range(1, n + 1):
            dsum = sum_digits(num)
            groups[dsum] += 1

            if groups[dsum] == largest:
                count += 1
            elif groups[dsum] > largest:
                largest = groups[dsum]
                count = 1

        return count

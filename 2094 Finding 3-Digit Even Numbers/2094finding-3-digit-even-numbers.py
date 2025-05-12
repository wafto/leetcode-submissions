class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        ans = []

        def counter_num(num: int) -> bool:
            numcount = Counter()
            while num > 0:
                numcount[num % 10] += 1
                num //= 10
            for number, counter in numcount.items():
                if count[number] < counter:
                    return False
            return True
            
        for num in range(100, 1000, 2):
            if counter_num(num):
                ans.append(num)

        return ans


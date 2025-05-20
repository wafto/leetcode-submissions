class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives, tens = 0, 0

        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10 and fives == 0:
                return False
            elif bill == 10 and fives > 0:
                fives -= 1
                tens += 1
            elif bill == 20 and tens > 0 and fives > 0:
                fives -= 1
                tens -= 1
            elif bill == 20 and fives >= 3:
                fives -= 3
            else:
                return False

        return True

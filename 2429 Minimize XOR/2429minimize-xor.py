class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        count1, count2 = bin(num1).count('1'), bin(num2).count('1')

        if count1 == count2:
            return num1

        curr = 1
        diff = count2 - count1

        while diff != 0:
            if diff < 0 and (num1 & curr) != 0:
                num1 ^= curr
                diff += 1
            elif diff > 0 and (num1 & curr) == 0:
                num1 |= curr
                diff -= 1
            curr <<= 1 
        
        return num1

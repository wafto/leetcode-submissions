class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        countS1 = [0] * 26
        countS2 = [0] * 26
        index = 0

        while index < n1:
            countS1[ord(s1[index]) - 97] += 1
            countS2[ord(s2[index]) - 97] += 1
            index += 1

        if countS1 == countS2:
            return True

        while index < n2:
            countS2[ord(s2[index - n1]) - 97] -= 1
            countS2[ord(s2[index]) - 97] += 1

            if countS1 == countS2:
                return True

            index += 1
            
        return False

        

            


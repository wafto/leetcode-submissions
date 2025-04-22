class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        output = 0
        acc1 = 1

        for i in range(n1 - 1, -1, -1):
            acc2 = 1
            for j in range(n2 - 1, -1, -1):
                output += int(num1[i]) * int(num2[j]) * acc1 * acc2
                acc2 *= 10
            acc1 *= 10

        return str(output)
        

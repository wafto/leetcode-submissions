class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        size = len(digits)
        carry = 1
        
        for i in range(size):
            index = size - 1 - i
            total = digits[index] + carry
            digits[index] = total % 10
            carry = 1 if total >= 10 else 0

        if carry == 1:
            digits.insert(0, 1)

        return digits
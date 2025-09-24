class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            return '0'

        fraction = []

        if numerator * denominator < 0:
            fraction.append('-')

        num, den = abs(numerator), abs(denominator)

        fraction.append(str(num // den))
        
        remain = num % den

        if remain == 0:
            return ''.join(fraction)

        fraction.append('.')

        lookup = {}
        
        while remain != 0:
            if remain in lookup:
                fraction.insert(lookup[remain], "(")
                fraction.append(')')
                break

            lookup[remain] = len(fraction)
            remain *= 10
            fraction.append(str(remain // den))
            remain %= den

        return ''.join(fraction)

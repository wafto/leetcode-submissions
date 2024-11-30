class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = {
            "M":  1000,
            "CM": 900,
            "D":  500,
            "CD": 400,
            "C":  100,
            "XC": 90,
            "L":  50,
            "XL": 40,
            "X":  10,
            "IX": 9,
            "V":  5,
            "IV": 4,
            "I":  1 
        }

        output = 0
        size = len(s)
        index = 0
        
        while index < size:
            if s[index:index + 2] in symbols:
                output += symbols[s[index:index + 2]]
                index += 2
            else:
                output += symbols[s[index]]
                index += 1

        return output


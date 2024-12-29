class Solution:
    def __init__(self):
        self.mapping = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "One Hundred",
            200: "Two Hundred",
            300: "Three Hundred",
            400: "Four Hundred",
            500: "Five Hundred",
            600: "Six Hundred",
            700: "Seven Hundred",
            800: "Eight Hundred",
            900: "Nine Hundred",
        }

        self.tmb = {
            3: "Thousand",
            6: "Million",
            9: "Billion",
        }

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        d = [int(n) for n in str(num)]
        words = []

        for i in range(len(d)):
            j = len(d) - 1 - i
            k = j % 3
            n = d[i] * (10 ** k)
        
            if n in self.mapping:
                if words and words[-1] == self.mapping[10] and k == 0:
                    words[-1] = self.mapping[n + 10]
                else:
                    words.append(self.mapping[n])
                                    
            if j in [3, 6, 9] and words[-1] not in self.tmb.values():
                words.append(self.tmb[j])

        return " ".join(words)


        
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = [str(i + 1) for i in range(n)]

        for i in range(len(output)):
            d3 = (i + 1) % 3 == 0
            d5 = (i + 1) % 5 == 0
            if d3 and d5:
                output[i] = "FizzBuzz"
                continue

            if d3:
                output[i] = "Fizz"
                continue
            
            if d5:
                output[i] = "Buzz"
        
        return output

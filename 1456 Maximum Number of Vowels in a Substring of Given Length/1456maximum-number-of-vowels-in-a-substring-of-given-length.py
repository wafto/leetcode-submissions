class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0

        for i in range(k):
            if s[i] in vowels:
                count += 1
            
        left, maximum = 0, count
        
        for right in range(k, len(s)):
            if s[left] in vowels:
                count -= 1
            if s[right] in vowels:
                count += 1
            maximum = max(maximum, count)
            left += 1

        return maximum



        

        
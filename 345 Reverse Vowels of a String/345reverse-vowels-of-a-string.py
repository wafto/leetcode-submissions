class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        data = list(s)
        left, right = 0, len(data) - 1

        while left < right:
            if data[left] not in vowels:
                left += 1
            elif data[right] not in vowels:
                right -= 1
            else:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1
                
        return ''.join(data)


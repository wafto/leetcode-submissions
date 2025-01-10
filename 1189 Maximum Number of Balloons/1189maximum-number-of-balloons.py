class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = [0] * 26

        for c in text:
            counter[ord(c) - 97] += 1
        
        r = [
            counter[ord('b') - 97] // 1,
            counter[ord('a') - 97] // 1,
            counter[ord('l') - 97] // 2,
            counter[ord('o') - 97] // 2,
            counter[ord('n') - 97] // 1,
        ]

        return min(r)

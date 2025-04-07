class Solution:
    def reverseWords(self, s: str) -> str:
        
        def split(sentence: str) -> List[str]:
            left, n = 0, len(sentence)
            words, word = [], deque()

            for right in range(n):
                if sentence[right] != ' ':
                    word.append(sentence[right])
                    continue
                
                if word:
                    words.append(''.join(word))
                    word.clear()
            if word:
                words.append(''.join(word))

            return words

        def reverse(words: List[str]) -> None:
            left, right = 0, len(words) - 1
            while left < right:
                words[left], words[right] = words[right], words[left]
                left, right = left + 1, right - 1
    
        words = split(s)
        reverse(words)

        return ' '.join(words)
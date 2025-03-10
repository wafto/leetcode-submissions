class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        def is_vowel(c: str) -> bool:
            return c in {'a', 'e', 'i', 'o', 'u'}

        def atleastk(word: str, k):
            left, ans, consonants = 0, 0, 0
            vowels = defaultdict(int)

            for right in range(len(word)):
                if is_vowel(word[right]):
                    vowels[word[right]] += 1
                else:
                    consonants += 1

                while len(vowels) == 5 and consonants >= k:
                    ans += len(word) - right
                    if is_vowel(word[left]):
                        vowels[word[left]] -= 1
                        if vowels[word[left]] == 0:
                            del vowels[word[left]]
                    else:
                        consonants -= 1
                    left += 1
            
            return ans

        return atleastk(word, k) - atleastk(word, k + 1)
        
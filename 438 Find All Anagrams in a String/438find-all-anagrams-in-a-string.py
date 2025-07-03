class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ord_a, compare = ord('a'), [0] * 26
        
        for c in p:
            compare[ord(c) - ord_a] += 1

        compare = tuple(compare)
        current, left, ans = [0] * 26, 0, []

        for right in range(len(s)):
            while right - left + 1 > len(p):
                current[ord(s[left]) - ord_a] -= 1
                left += 1

            current[ord(s[right]) - ord_a] += 1
            
            if right - left + 1 == len(p) and compare == tuple(current):
                ans.append(left)
            
        return ans


                            


        
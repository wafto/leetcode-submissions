class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left, ones = 0, 0
        smallest = ''

        for right in range(len(s)):
            ones += 1 if s[right] == '1' else 0

            while ones == k:
                if not smallest:
                    smallest = s[left: right + 1]
                
                elif (right - left + 1) < len(smallest):
                    smallest = s[left: right + 1]
                
                elif (right - left + 1) == len(smallest):
                    smallest = min(smallest, s[left: right + 1])
                    
                ones -= 1 if s[left] == '1' else 0
                left += 1

        return smallest

                
            
            

            
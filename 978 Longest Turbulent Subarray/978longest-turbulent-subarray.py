class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        output = 1
        prev = ''

        while r < len(arr):
            if arr[r - 1] < arr[r] and prev != '<':
                output = max(output, r - l + 1)
                r += 1
                prev = '<'
                continue
            if arr[r - 1] > arr[r] and prev != '>':
                output = max(output, r - l + 1)
                r += 1
                prev = '>'
                continue
            if arr[r - 1] == arr[r]:
                r += 1        
            l = r - 1
            prev = ''
        
        return output

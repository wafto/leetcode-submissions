class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        licence = []
        acc = []
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '-':
                continue
            
            acc.append(s[i].upper())
            
            if len(acc) == k:
                acc.reverse()
                licence.append(''.join(acc))
                acc = []
        
        if acc:
            acc.reverse()
            licence.append(''.join(acc))
        
        licence.reverse()
        
        return '-'.join(licence)
        
        
        
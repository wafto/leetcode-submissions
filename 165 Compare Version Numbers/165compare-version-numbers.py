class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        def normalize(version: str) -> List[int]:
            return [int(sub) for sub in version.split('.')]

        v1, v2 = normalize(version1), normalize(version2)
        n1, n2 = len(v1), len(v2)

        for i in range(max(n1, n2)):
            sub1 = v1[i] if i < n1 else 0
            sub2 = v2[i] if i < n2 else 0

            if sub1 > sub2:
                return 1
            elif sub1 < sub2:
                return -1
        
        return 0

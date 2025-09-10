class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        toteach = set()
        
        for u, v in friendships:
            u, v = u - 1, v - 1
            can_communicate = False

            for lang in languages[u]:
                if lang in languages[v]:
                    can_communicate = True
                    break

            if not can_communicate:
                toteach.add(u)
                toteach.add(v)

        min_users_to_teach = float('inf')

        for lang in range(1, n + 1):
            count = 0
            
            for u in toteach:
                count += 1 if lang not in languages[u] else 0
            
            min_users_to_teach = min(min_users_to_teach, count)

        return min_users_to_teach
        
        
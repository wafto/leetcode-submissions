class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people)
        L, R = 0, len(people) - 1
        boats = 0

        while L <= R:
            if people[L] + people[R] <= limit:
                L += 1
                R -= 1
            else:
                R -= 1
            boats += 1

        return boats

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # [1, 2, 2, 3, 3]
        # [1 2 4 5]
        """
        
        """
        people.sort()
        t = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            if people[i] + people[j] <= limit:
                t += 1
                i += 1
                j -= 1
            else:
                t += 1
                j -= 1
        return t
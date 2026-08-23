import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1, 4, 3, 2]

        # b/h = k 
        # [1, 2, 3, 4, 5, 6, 7, 8, 9]
        arr = []
        min_speed = max(piles) + 1
        l = 0
        r = max(piles)
        
        while l <= r:
            k = (l + r) // 2
            if k == 0:
                l = k + 1
                continue
            accum_hour = 0
            for pile in piles:
                accum_hour += math.ceil(pile/k)
            if accum_hour <= h:
                min_speed = k
                r = k - 1
            else:
                l = k + 1
        return min_speed
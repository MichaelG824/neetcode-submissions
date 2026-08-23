class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        slowest_time = 0
        fleets = 0
        # target = 10 - 7 / 1 
        for p, s in pair:
            d = target - p
            time = d / s
            if time > slowest_time:
                slowest_time = time
                fleets += 1
        return fleets
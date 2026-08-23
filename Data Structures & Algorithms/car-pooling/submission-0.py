import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 
        trips.sort(key=lambda t: t[1])  # sort by start location
        pq = []  # (drop_off_location, passengers)
        curr = 0
        for num, start, end in trips:
            while pq and pq[0][0] <= start:
                curr -= pq[0][1]
                heapq.heappop(pq)
            curr += num
            if curr > capacity:
                return False
            heapq.heappush(pq, (end, num))
        return True 



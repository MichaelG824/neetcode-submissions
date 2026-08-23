import queue

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = queue.PriorityQueue()

        for x, y in points:
            dist = x**2 + y**2
            pq.put((dist, x, y))
        res = []
        for _ in range(k):
            dist, x, y = pq.get()
            res.append([x, y])
        return res
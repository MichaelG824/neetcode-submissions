import queue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = queue.PriorityQueue()

        # O(nlogn)
        for s in stones:
            pq.put(-s)
        
        while pq.qsize() > 1:
            f = pq.get()
            sec = pq.get()
            new_val = abs(abs(f) - abs(sec))
            if new_val != 0:
                pq.put(-new_val)
            print(new_val)
        if pq.qsize() > 0:
            val = pq.get()
            return abs(val)
        return 0
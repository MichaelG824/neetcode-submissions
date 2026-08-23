import queue
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        AAA B C
        Track max priority queue for 

        """
        time = 0
        count = Counter(tasks)

        pq = queue.PriorityQueue()
        cooldown_q = deque() # (-3, time)
        for c in count.values():
            pq.put(-c)
        
        while pq.qsize() > 0 or cooldown_q:
            time += 1
            if pq.qsize() > 0:
                cnt = pq.get()
                cnt += 1
                if cnt:
                    cooldown_q.append((cnt, time + n))
            if cooldown_q and time == cooldown_q[0][1]:
                pq.put(cooldown_q[0][0])
                cooldown_q.popleft()
        return time
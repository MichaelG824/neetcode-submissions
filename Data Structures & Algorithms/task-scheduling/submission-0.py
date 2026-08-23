import queue
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        XXYY 

        """
        count = Counter(tasks)
        max_pq = queue.PriorityQueue()
        cooldown_queue = deque()
        for c in count.values():
            max_pq.put(-c)
        time = 0
        while max_pq.qsize() > 0 or cooldown_queue:
            time += 1
            if max_pq.qsize() > 0:
                c = max_pq.get()
                cnt = 1 + c
                if cnt:
                    cooldown_queue.append((cnt, time + n))
            if cooldown_queue and cooldown_queue[0][1] == time:
                max_pq.put(cooldown_queue[0][0])
                cooldown_queue.popleft()
        return time
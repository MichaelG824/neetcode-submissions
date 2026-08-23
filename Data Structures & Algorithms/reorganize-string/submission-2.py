from queue import PriorityQueue
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        if max(count.values()) > (len(s) + 1) // 2:
            return ""
        pq = PriorityQueue()
        for k, v in count.items():
            pq.put((-v, k))
        # y
        # (-2, y), (-1, x), ()
        res = []

        prev = None

        while pq.qsize() > 0:
            count, char = pq.get()
            if prev == char:
                new_count, new_char = pq.get()
                new_count += 1
                res.append(new_char)
                if new_count:
                    pq.put((new_count, new_char))
                pq.put((count, char))
                prev = new_char
            else:
                res.append(char)
                count += 1
                if count:
                    pq.put((count, char))
                prev = char
        return ''.join(res)

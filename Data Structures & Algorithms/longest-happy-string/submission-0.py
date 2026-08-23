from queue import PriorityQueue

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = PriorityQueue()

        if a:
            pq.put((-a, "a"))
        if b:
            pq.put((-b, "b"))
        if c:
            pq.put((-c, "c"))
        
        # (char, count)
        prev = None

        res = []
        # if prev and prev[0] == char and prev[1] == count:
            # if pq is empty then return res immediately 
            # otherwise use next highest priority char and update res and char

        # else update and add res  
        while pq.qsize() > 0:
            count, char = pq.get()
            if prev and prev[1] == char and prev[0] == 2:
                print(char, count, "If statement")
                if not pq.qsize():
                    return ''.join(res)
                new_count, new_char = pq.get()
                res.append(new_char)
                prev = (0, new_char)
                if new_count + 1 < 0:
                    pq.put((new_count + 1, new_char))
                pq.put((count, char))
            else:
                print(char, count)
                res.append(char)
                prev_count = prev[0] if prev else 0
                prev = (prev_count + 1, char)
                if count + 1 < 0:
                    pq.put((count + 1, char))
            
        # else update and add res 
        return ''.join(res)
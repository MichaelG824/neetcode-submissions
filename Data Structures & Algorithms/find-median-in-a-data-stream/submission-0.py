import heapq
class MedianFinder:

    def __init__(self):
        # max_heap min heap
        # 1 2     3 4 5
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)
    # O(log(n))
    def addNum(self, num: int) -> None:
        if self.min_heap and num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, -num)
        
        if len(self.max_heap) >= len(self.min_heap) + 1:
            val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -val)
        elif len(self.min_heap) >= len(self.max_heap) + 1:
            val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -val)

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        val1 = self.min_heap[0]
        val2 = self.max_heap[0]
        return (val1 + -val2) / 2

        
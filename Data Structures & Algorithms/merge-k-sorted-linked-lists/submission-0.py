# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        [[1, 2, 4], [1, 3, 5], [3, 6]]
        """
        # [[1,2,4],[1,3,5],[3,6]]
        heap = []
        heapq.heapify(heap)
        counter = count()
        for i in range(len(lists)):
            node = lists[i]
            heapq.heappush(heap, (node.val, next(counter), node))
        
        dummy = ListNode(0)
        curr = dummy
        while heap:
            c_obj = heapq.heappop(heap)
            node = c_obj[2]
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val,next(counter), node.next))
        return dummy.next
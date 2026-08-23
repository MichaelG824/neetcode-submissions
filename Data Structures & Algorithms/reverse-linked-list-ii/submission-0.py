# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # 0 -> 1 -> 3 -> 2 -> 4 -> 5
        # 0 -> 2 -> 1 -> 3 -> 4 -> 5
        # 
        dummy = ListNode(0, head)
        
        # reach node with position left. 
        left_prev, curr = dummy, head
        for i in range(left - 1):
            left_prev = curr
            curr = curr.next

        prev = None

        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        left_prev.next.next = curr
        left_prev.next = prev

        return dummy.next

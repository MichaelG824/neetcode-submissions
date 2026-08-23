# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = l1
        curr_2 = l2
        dummy_node = ListNode(0)
        curr = ListNode(0)
        dummy_node.next = curr
        carry = 0
        while curr_1 or curr_2:
            temp_sum = 0
            if curr_1:
                temp_sum += curr_1.val
                curr_1 = curr_1.next
            if curr_2:
                temp_sum += curr_2.val
                curr_2 = curr_2.next
            curr.val = (temp_sum + carry) % 10 
            carry = (temp_sum + carry) // 10
            if curr_1 or curr_2 or carry > 0:
                curr.next = ListNode(carry)
                curr = curr.next
        return dummy_node.next
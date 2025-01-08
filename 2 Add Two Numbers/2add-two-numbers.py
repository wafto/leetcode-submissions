# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        aux1 = l1
        aux2 = l2
        tail = head

        carry = 0

        while aux1 != None or aux2 != None:
            total = carry
            
            if aux1:
                total += aux1.val
                aux1 = aux1.next
            
            if aux2:
                total += aux2.val
                aux2 = aux2.next
                
            carry = total // 10 

            tail.next = ListNode(total % 10)
            tail = tail.next

        if carry == 1:
            tail.next = ListNode(1)

        return head.next
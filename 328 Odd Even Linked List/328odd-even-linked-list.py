# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ohead, ehead = ListNode(0), ListNode(0)
        oaux, eaux, curr = ohead, ehead, head
        n = 0

        while curr:
            tmp = curr.next
            curr.next = None
            n += 1
            if n & 1 == 0:
                oaux.next = curr
                oaux = oaux.next
            else:
                eaux.next = curr
                eaux = eaux.next
            curr = tmp
        
        eaux.next = ohead.next

        return ehead.next
        
        
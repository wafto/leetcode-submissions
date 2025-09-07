# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ohead = opointer = ListNode(-1)
        ehead = epointer = ListNode(-1)
        num, curr = 0, head

        while curr:
            if num & 1:
                opointer.next = curr
                opointer = opointer.next
            else:
                epointer.next = curr
                epointer = epointer.next
            curr = curr.next
            num += 1

        opointer.next = None
        epointer.next = ohead.next

        return ehead.next

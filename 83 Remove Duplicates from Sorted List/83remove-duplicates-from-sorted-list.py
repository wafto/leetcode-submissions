# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nhead = ListNode(-100)
        curr = nhead
        aux = head

        while aux:
            if aux.val != curr.val:
                curr.next = aux
                curr = curr.next
            aux = aux.next

        curr.next = None
        return nhead.next
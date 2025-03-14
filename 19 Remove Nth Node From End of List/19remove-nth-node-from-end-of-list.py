# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sz, curr = 0, head

        while curr:
            curr = curr.next
            sz += 1

        index = sz - n

        if index == 0:
            return None if sz == 1 else head.next

        prev, curr, i = None, head, 0

        while i < index:
            prev = curr
            curr = curr.next
            i += 1

        prev.next = curr.next

        return head
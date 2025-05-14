# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode(0)
        p, p1, p2 = sentinel, list1, list2

        while p1 and p2:
            if p1.val <= p2.val:
                sentinel.next = p1
                p1 = p1.next
            else:
                sentinel.next = p2
                p2 = p2.next
            sentinel = sentinel.next

        if p1:
            sentinel.next = p1

        if p2:
            sentinel.next = p2

        return p.next



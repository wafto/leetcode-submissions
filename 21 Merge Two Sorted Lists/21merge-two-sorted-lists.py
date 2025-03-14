# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = list1, list2
        nhead = ListNode(0)
        sentinel = nhead

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                sentinel.next = curr1
                curr1 = curr1.next
            else:
                sentinel.next = curr2
                curr2 = curr2.next
            sentinel = sentinel.next

        while curr1:
            sentinel.next = curr1
            sentinel = sentinel.next
            curr1 = curr1.next

        while curr2:
            sentinel.next = curr2
            sentinel = sentinel.next
            curr2 = curr2.next

        return nhead.next
        

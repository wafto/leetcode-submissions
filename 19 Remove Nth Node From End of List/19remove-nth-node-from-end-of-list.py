# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length, curr = 0, head

        while curr:
            length += 1
            curr = curr.next

        prev = head
        index = length - n - 1

        if index == -1:
            return head.next

        count = 0
        while prev and count < index:
            count += 1
            prev = prev.next

        if not prev:
            return head

        if prev and prev.next:
            prev.next = prev.next.next

        return head

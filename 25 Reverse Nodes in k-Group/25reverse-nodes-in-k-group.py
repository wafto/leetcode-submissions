# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Not empty list
        if not head:
            return head

        # At least k elements
        tail = head
        for _ in range(k):
            if not tail:
                return head
            tail = tail.next

        prev, curr = None, head

        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head.next = self.reverseKGroup(tail, k)
        return prev

        
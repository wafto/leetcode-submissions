# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr, ahead = None, head, head

        while n > 0 and ahead:
            ahead = ahead.next
            n -= 1

        while ahead:
            prev = curr
            curr = curr.next
            ahead = ahead.next

        if not prev and not curr:
            return None
        if not prev:
            return curr.next
        
        prev.next = curr.next

        return head
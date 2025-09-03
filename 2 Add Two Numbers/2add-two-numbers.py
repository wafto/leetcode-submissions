# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nhead = ListNode(-1)
        curr, p1, p2, carry = nhead, l1, l2, 0

        while p1 or p2:
            total = (p1.val if p1 else 0) + (p2.val if p2 else 0) + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None

        if carry:
            curr.next = ListNode(1)

        return nhead.next


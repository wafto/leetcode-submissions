# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left, right = head, head

        while k > 1:
            left = left.next
            k -= 1

        tail = left
        while tail.next:
            right = right.next
            tail = tail.next

        left.val, right.val = right.val, left.val

        return head
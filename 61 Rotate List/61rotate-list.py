# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head 
        
        last, size = head, 1
        
        while last and last.next:
            last = last.next
            size += 1

        k = k % size
        last.next = head

        curr, move = last, size - k

        while move > 0:
            curr = curr.next
            move -= 1

        nhead = curr.next
        curr.next = None
        return nhead




        

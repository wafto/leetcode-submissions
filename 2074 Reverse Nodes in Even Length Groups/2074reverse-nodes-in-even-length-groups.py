# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node:
                return None            
            prev, curr = None, node
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        group = 1
        curr = head
        
        nhead = ListNode(-1)
        nlast = nhead

        while curr:
            start, end = curr, curr
            length = 0
            
            for j in range(group):
                if not curr:
                    break
                end = curr
                curr = curr.next
                length += 1
                
            if length & 1 == 0:
                end.next = None
                end = start
                nlast.next = reverse(start)
            else:
                nlast.next = start
                
            nlast = end
            group += 1

        return nhead.next

        
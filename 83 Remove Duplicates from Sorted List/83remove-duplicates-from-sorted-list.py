# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        first, second = head, head.next
        
        while second:
            while second and first.val == second.val:
                second = second.next
            
            first.next = second
            first = first.next
            
        return head
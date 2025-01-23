# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        I, J, L, R = 1, 1, head, None
        PREV, NEXT = None, None
        
        while L and I < left:
            I += 1
            PREV = L
            L = L.next
        
        R = L
        J = I
        
        while R and J < right:
            J += 1
            R = R.next
        
        NEXT = R.next
        AUX = PREV
        NL = L
        
        while NL != NEXT:
            TMP = NL.next 
            NL.next = AUX
            AUX = NL
            NL = TMP

        if PREV:
            PREV.next = R
        else:
            head = R
        
        L.next = NEXT

        return head


